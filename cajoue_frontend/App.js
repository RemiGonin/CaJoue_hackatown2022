import { React, useState, useEffect } from "react";
import { StyleSheet, Text, View, Dimensions, TouchableOpacity, Picker } from "react-native";
import MapView from "react-native-maps";
import { Marker, Callout } from "react-native-maps";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import openMap from "react-native-open-maps";

function MapCajoue({ navigation }) {
    const [patinoires, setPatinoires] = useState([]);
    const [isLoading, setLoading] = useState(true);

    const montrealRegion = { latitude: 45.505, longitude: -73.614, latitudeDelta: 0.0922, longitudeDelta: 0.0421 };

    //runs every second, fetch all database
    useEffect(() => {
        const interval = setInterval(() => {
            fetch("http://51.222.45.99:8000/patinoires?opt=all")
            .then((response) => response.json())
            .then((json) => setPatinoires(json))
            .catch((error) => console.error(error))
            .finally(() => setLoading(false));
          }, 1000)
          return () => clearInterval(interval)
    }, []);

  
    //only need to do once ??
    patinoires.forEach(
        (patinoire) =>
            (patinoire.coordinates = {
                latitude: patinoire.lat,
                longitude: patinoire.lng,
            })
    );

    return (
        <View style={styles.container}>
            <MapView style={styles.map} initialRegion={montrealRegion}>
                {patinoires.map((marker, index) => (
                    <Marker
                        key={index}
                        title={marker.nom}
                        description={marker.description}
                        coordinate={marker.coordinates}
                        onCalloutPress={() => navigation.navigate("Details", { marker })}
                        icon={
                            marker.jeu * 1000 > Date.now()
                                ? require("./assets/markerCaJoue.png")
                                : marker.ouvert
                                ? require("./assets/markerCaJouePas.png")
                                : require("./assets/markerFerme.png")
                        }
                    >
                        <Callout tooltip>
                            <View>
                                <View style={styles.bubble}>
                                    <Text style={styles.name}>{marker.nom}</Text>
                                    <Text>{marker.description}</Text>
                                    <Text style={marker.ouvert ? styles.ouvert : styles.fermee}>{marker.ouvert ? "Ouvert" : "Fermé"}</Text>

                                    <Text style={styles.CaJoue}>{marker.jeu * 1000 > Date.now() ? "Ca joue !" : ""}</Text>
                                </View>
                            </View>
                        </Callout>
                    </Marker>
                ))}
            </MapView>
        </View>
    );
}

function DetailsScreen({ route, navigation }) {
    const [selectedValue, setSelectedValue] = useState("30");
    const marker = route.params;
    return (
        <View style={{ flex: 1, alignItems: "center" }}>
            <Text style={styles.name}>
                {"\n"}
                {"\n"}
                {"\n"}
                {"\n"}
                {marker.marker.nom}
            </Text>
            <Text>{marker.marker.adresse}</Text>
            <Text>Type : {marker.marker.description}</Text>
            <Text style={marker.marker.ouvert ? styles.ouvert : styles.fermee}>
                {marker.marker.ouvert ? "Cette patinoire est ouverte" : "Cette patinoire semble fermée pour l'instant..."}
            </Text>

            {marker.marker.jeu * 1000 > Date.now() ? (
                <Text style={styles.CaJoue}>
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}Ça joue ! {"\n"}
                    {"\n"}
                    <TouchableOpacity style={styles.button} onPress={() => openMap({ end: marker.marker.adresse })}>
                        <Text>S'y rendre</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                        style={styles.buttonCaJouePlus}
                        onPress={() => fetch('http://51.222.45.99:8000/patinoires/'+marker.marker.id+'/cajoueplus', {
                            method: "PUT",
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json'
                            },
                        })}
                        
                    >
                        <Text>Ça joue plus</Text>
                    </TouchableOpacity>
                </Text>
            ) : (
                <View>
                    <Text>
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                    {"\n"}
                        Je veux chercher des partenaires pendant :</Text>
                    <Picker
                        selectedValue={selectedValue}
                        style={{ height: 50, width: 150 }}
                        onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
                    >
                        <Picker.Item label="10 minutes" value="10" />
                        <Picker.Item label="20 minutes" value="20" />
                        <Picker.Item label="30 minutes" value="30" />
                        <Picker.Item label="40 minutes" value="40" />
                        <Picker.Item label="50 minutes" value="50" />
                        <Picker.Item label="60 minutes" value="60" />
                    </Picker>
                    <Text>
                    {"\n"}
                    </Text>

                    <TouchableOpacity onPress={() => fetch('http://51.222.45.99:8000/patinoires/'+marker.marker.id+'/cajoue?duration='+ selectedValue, {
                        method: "PUT",
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                    })}>
                        <View style={styles.button}>
                            <Text>Jouer !</Text>
                        </View>
                    </TouchableOpacity>
                </View>
            )}
        </View>
    );
}

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName="Cajoue">
                <Stack.Screen name="CaJoue" component={MapCajoue} />
                <Stack.Screen name="Details" component={DetailsScreen} />
            </Stack.Navigator>
        </NavigationContainer>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
        justifyContent: "center",
    },

    button: {
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "rgba(255, 193, 7, 1)",
        padding: 10,
        marginHorizontal: 50,
        height: 50,
        width: 200,
        marginVertical: 10,
        borderRadius: 5,
    },

    buttonCaJoue: {
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "rgba(255, 193, 7, 1)",
        padding: 10,
        marginHorizontal: 50,
        height: 50,
        width: 200,
        marginVertical: 10,
        borderRadius: 5,
    },

    buttonCaJouePlus: {
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "rgba(255, 1, 7, 1)",
        padding: 10,
        marginHorizontal: 50,
        height: 50,
        width: 200,
        marginVertical: 10,
        borderRadius: 5,
    },

    map: {
        width: Dimensions.get("window").width,
        height: Dimensions.get("window").height,
    },

    bubble: {
        flex: 1,
        backgroundColor: "rgba(255,255,255,1)",
        paddingHorizontal: 18,
        paddingVertical: 12,
        borderRadius: 10,
    },

    name: {
        fontSize: 16,
        fontWeight: "bold",
        marginBottom: 4,
    },

    ouvert: {
        color: "green",
    },

    fermee: {
        color: "red",
    },

    CaJoue: {
        color: "orange",
        fontWeight: "bold",
        fontSize: 16,
    },
});

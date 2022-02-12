import { React, useState } from "react";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, Dimensions } from "react-native";
import MapView from "react-native-maps";
import { Marker } from "react-native-maps";

export default function App() {
    const montrealRegion = { latitude: 45.505, longitude: -73.614, latitudeDelta: 0.0922, longitudeDelta: 0.0421 };

    return (
        <View style={styles.container}>
            <Text>test12345</Text>
            <StatusBar style="auto" />

            <MapView style={styles.map} initialRegion={montrealRegion}>
                <Marker coordinate={montrealRegion} />
            </MapView>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
        justifyContent: "center",
    },

    map: {
        width: Dimensions.get("window").width,
        height: Dimensions.get("window").height,
    },
});

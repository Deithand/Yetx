import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("YetX")

    Rectangle {
        anchors.fill: parent
        color: "#202020"

        Text {
            anchors.centerIn: parent
            color: "white"
            text: qsTr("YetX")
        }
    }
}

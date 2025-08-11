import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("YetX")

    Column {
        anchors.centerIn: parent
        spacing: 8

        TextField {
            id: magnetInput
            width: 400
            placeholderText: qsTr("Magnet URI")
        }

        Button {
            text: qsTr("Add Torrent")
            onClicked: {
                controller.add_magnet(magnetInput.text)
                magnetInput.text = ""
            }
        }

        ListView {
            width: 400
            height: 300
            model: torrentModel
            delegate: Text { text: modelData }
        }
    }
}

import asyncio
from gravitraxconnect import gravitrax_bridge, gravitrax_constants


async def send_signal_to_starter():
    # Bridge-Objekt erstellen
    bridge = gravitrax_bridge.GravitraxBridge()

    try:
        # Suche nach einem GraviTrax Connect-Gerät und verbinde dich
        print("Suche nach GraviTrax Connect...")
        await bridge.connect()
        print(f"Verbunden mit {bridge.name}")

        # Signal an den Starter senden (Farbe: Rot, alle Starter)
        # Signaltyp: Execute (direkte Ausführung)
        print("Sende Signal an den Starter...")
        await bridge.send_signal(
            gravitrax_constants.STONE_STARTER,  # Ziel: Starter
            gravitrax_constants.COLOR_RED,  # Farbe: Rot
            gravitrax_constants.SIGNAL_EXECUTE,  # Signal: Ausführen
        )
        print("Signal erfolgreich gesendet!")

    except Exception as e:
        print(f"Fehler: {e}")

    finally:
        # Verbindung trennen
        await bridge.disconnect()
        print("Verbindung getrennt.")


# Asynchrones Programm ausführen
if __name__ == "__main__":
    asyncio.run(send_signal_to_vstarter())

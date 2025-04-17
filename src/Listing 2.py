import time
import threading


# Callback-Funktion, die ausgeführt wird, wenn ein Signal erkannt wird
def on_signal_received(signal_data):
    print(f"Signal erhalten: {signal_data}")
    # Hier könnte beispielsweise eine GraviTrax-Aktion ausgelöst werden
    print("GraviTrax-Aktion: Kugel wird freigegeben oder Stopper bewegt!")


# Klasse für das GraviTrax-System
class GraviTraxSystem:
    def __init__(self):
        self.running = False
        self.callback = None

    # Methode zum Registrieren der Callback-Funktion
    def register_callback(self, callback_func):
        self.callback = callback_func
        print("Callback-Funktion registriert.")

    # Simulierte Methode, die auf Signale wartet (z.B. von einem Sensor)
    def listen_for_signal(self):
        self.running = True
        print("Warte auf Signale...")
        signal_count = 0
        while self.running:
            # Simuliertes Signal (z.B. alle 3 Sekunden für Demo-Zwecke)
            time.sleep(3)
            signal_count += 1
            signal_data = f"Signal #{signal_count} - Zeit: {time.ctime()}"

            # Wenn ein Signal erkannt wird und ein Callback registriert ist, führe es aus
            if self.callback:
                self.callback(signal_data)

            # Beende die Schleife nach 3 Signalen
            if signal_count >= 3:
                self.stop()

    # Methode zum Stoppen des Systems
    def stop(self):
        self.running = False
        print("GraviTrax-System gestoppt.")


# Hauptprogramm
def main():
    # Erstelle Instanz des GraviTrax-Systems
    gravitraSystem = GraviTraxSystem()

    # Registriere die Callback-Funktion
    gravitraSystem.register_callback(on_signal_received)

    # Starte das System in einem separaten Thread, um Signale zu empfangen
    listener_thread = threading.Thread(target=gravitraSystem.listen_for_signal)
    listener_thread.start()

    # Warte, bis der Thread beendet ist
    listener_thread.join()


if __name__ == "__main__":
    main()

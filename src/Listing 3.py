import asyncio
async def monitor_trigger(channel):
print(f“Warte auf Trigger-Signal (Kanal {channel})...“)
  await asyncio.sleep(2)
  print(f“Trigger auf Kanal {channel} aktiviert!“)
  return channel
async def activate_starter(channel):
  print(f“Starter auf Kanal {channel} wird ausgelöst!“)
  await asyncio.sleep(1)
  print(f“Starter auf Kanal {channel} abgeschlossen.“)
async def main():
 trigger_task = monitor_trigger(“Rot“)
 starter_task = activate_starter(“Rot“)
 await asyncio.gather(trigger_task, starter_task)
asyncio.run(main())
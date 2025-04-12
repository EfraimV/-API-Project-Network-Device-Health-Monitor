from fastapi import FastAPI
from cisco_client import CiscoDevice

app = FastAPI(title="Network Health API")

@app.get("/health/{ip}")
async def device_health(ip: str):
    """Checks device vitals: CPU, memory, BGP neighbors"""
    device = CiscoDevice(ip)
    return {
        "cpu_load": device.get_cpu(),
        "memory": device.get_memory(),
        "bgp_status": device.get_bgp_summary()
    }

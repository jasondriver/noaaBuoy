from buoyant import Buoy

def prettyPrintBuoy(buoy):
    print(f"Buoy Number: {buoy.id}")
    print(f"Buoy Coordinates: {buoy.coords}")
    print(f"eventtime: {buoy.eventtime}")
    print(f"image url: {buoy.image_url}")
    print(f"air_pressure_at_sea_level: {buoy.air_pressure_at_sea_level}")
    print(f"air_temperature: {buoy.air_temperature}")
    print(f"currents: {buoy.currents}")
    print(f"sea_floor_depth_below_sea_surface: {buoy.sea_floor_depth_below_sea_surface}")
    print(f"sea_water_electrical_conductivity: {buoy.sea_water_electrical_conductivity}")
    print(f"sea_water_salinity: {buoy.sea_water_salinity}")
    print(f"sea_water_temperature: {buoy.sea_water_temperature}")
    print(f"waves: {buoy.waves}")
    print(f"winds: {buoy.winds}")
    return

if __name__ == "__main__":
    buoy1 = Buoy(46026)  # farallon islands
    buoy2 = Buoy(46237)  # sf straights
    buoy3 = Buoy(46012)  # offshore monterey

    prettyPrintBuoy(buoy1)
    prettyPrintBuoy(buoy2)
    prettyPrintBuoy(buoy3)

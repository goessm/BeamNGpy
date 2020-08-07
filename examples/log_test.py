from beamngpy import BeamNGpy, Scenario, Vehicle, setup_logging

def main():
    print("hi")
    setup_logging()
    beamng = BeamNGpy('localhost', 64256)

    # Create a scenario in west_coast_usa
    scenario = Scenario('west_coast_usa', 'research_test',
                        description='Random driving for research')

    # Set up first vehicle, with two cameras, gforces sensor, lidar, electrical
    # sensors, and damage sensors
    vehicle = Vehicle('ego_vehicle', model='etk800',
                      licence='RED', color='Red')

    scenario.add_vehicle(vehicle, pos=(-717.121, 101, 118.675), rot=(0, 0, 45))

    # Compile the scenario and place it in BeamNG's map folder
    scenario.make(beamng)

    # Start BeamNG and enter the main loop
    bng = beamng.open(launch=True)
    try:
        bng.hide_hud()
        bng.set_deterministic()  # Set simulator to be deterministic
        bng.set_steps_per_second(60)  # With 60hz temporal resolution

        # Load and start the scenario
        bng.load_scenario(scenario)
        bng.start_scenario()
        bng.enable_vehicle_stats_logging()
        while 1:
            bng.step(20)

    finally:
        bng.close()
    



if __name__ == '__main__':
    main()

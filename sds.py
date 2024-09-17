data_centers = [
    {
        "name": "Amsterdam",
        "latency_to_metro": 10.2,  # ms
        "bandwidth": 13,  # Gbps
        "cost": 8,  # monthly cost in USD
        "power_consumption": 20,  # MW
        "carbon_emissions": 15,  # metric tons of CO2
        "water_usage": 50000,  # m³
    },
    {
        "name": "Bergen",
        "latency_to_metro": 4.3,  # ms
        "bandwidth": 7,  # Gbps
        "cost": 5,  # monthly cost in USD
        "power_consumption": 12,  # MW
        "carbon_emissions": 9,  # metric tons of CO2
        "water_usage": 35000,  # m³
    },
    {
        "name": "Copenhagen",
        "latency_to_metro": 7.5,  # ms
        "bandwidth": 14.3,  # Gbps
        "cost": 6,  # monthly cost in USD
        "power_consumption": 18,  # MW
        "carbon_emissions": 13,  # metric tons of CO2
        "water_usage": 45000,  # m³
    },
    {
        "name": "Dublin",
        "latency_to_metro": 8.6,  # ms
        "bandwidth": 18.3,  # Gbps
        "cost": 7,  # monthly cost in USD
        "power_consumption": 22,  # MW
        "carbon_emissions": 16,  # metric tons of CO2
        "water_usage": 55000,  # m³
    },
    {
        "name": "Esbjerg (DK01)",
        "latency_to_metro": 6.7,  # ms
        "bandwidth": 22.1,  # Gbps
        "cost": 14.5,  # monthly cost in USD
        "power_consumption": 25,  # MW
        "carbon_emissions": 19,  # metric tons of CO2
        "water_usage": 60000,  # m³
    },
    {
        "name": "Frankfurt",
        "latency_to_metro": 11.3,  # ms
        "bandwidth": 18,  # Gbps
        "cost": 12.6,  # monthly cost in USD
        "power_consumption": 20,  # MW
        "carbon_emissions": 15,  # metric tons of CO2
        "water_usage": 48000,  # m³
    },
    {
        "name": "Hamburg",
        "latency_to_metro": 7.6,  # ms
        "bandwidth": 14.9,  # Gbps
        "cost": 10.9,  # monthly cost in USD
        "power_consumption": 16,  # MW
        "carbon_emissions": 12,  # metric tons of CO2
        "water_usage": 42000,  # m³
    },
    {
        "name": "Kristiansand (NO1)",
        "latency_to_metro": 3.8,  # ms
        "bandwidth": 11,  # Gbps
        "cost": 75,  # monthly cost in USD
        "power_consumption": 30,  # MW
        "carbon_emissions": 25,  # metric tons of CO2
        "water_usage": 75000,  # m³
    },
    {
        "name": "London",
        "latency_to_metro": 7.8,  # ms
        "bandwidth": 19.4,  # Gbps
        "cost": 11,  # monthly cost in USD
        "power_consumption": 24,  # MW
        "carbon_emissions": 20,  # metric tons of CO2
        "water_usage": 60000,  # m³
    },
    {
        "name": "New Jersey",
        "latency_to_metro": 4,  # ms
        "bandwidth": 10,  # Gbps
        "cost": 6,  # monthly cost in USD
        "power_consumption": 15,  # MW
        "carbon_emissions": 11,  # metric tons of CO2
        "water_usage": 40000,  # m³
    },
    {
        "name": "Oslo (OS-IX)",
        "latency_to_metro": 3,  # ms
        "bandwidth": 6,  # Gbps
        "cost": 9,  # monthly cost in USD
        "power_consumption": 14,  # MW
        "carbon_emissions": 10,  # metric tons of CO2
        "water_usage": 35000,  # m³
    },
    {
        "name": "Paris",
        "latency_to_metro": 9,  # ms
        "bandwidth": 18.6,  # Gbps
        "cost": 14.6,  # monthly cost in USD
        "power_consumption": 21,  # MW
        "carbon_emissions": 18,  # metric tons of CO2
        "water_usage": 50000,  # m³
    },
    {
        "name": "Stavanger",
        "latency_to_metro": 8,  # ms
        "bandwidth": 7,  # Gbps
        "cost": 3.8,  # monthly cost in USD
        "power_consumption": 12,  # MW
        "carbon_emissions": 8,  # metric tons of CO2
        "water_usage": 30000,  # m³
    },
    {
        "name": "Stockholm",
        "latency_to_metro": 6,  # ms
        "bandwidth": 11,  # Gbps
        "cost": 3.8,  # monthly cost in USD
        "power_consumption": 10,  # MW
        "carbon_emissions": 7,  # metric tons of CO2
        "water_usage": 25000,  # m³
    },
]

# Define your requirements, for example:
desired_latency = 6  # ms or your desired value
desired_bandwidth = 15  # Gbps or your desired value
max_cost = 1200  # maximum monthly cost you're willing to pay

# Initialize variables for the best data center choice
best_data_center = None
best_score = float('inf')  # Initialize with positive infinity

# Evaluate data centers and find the best one
for center in data_centers:
    latency_score = abs(center["latency_to_metro"] - desired_latency)
    bandwidth_score = abs(center["bandwidth"] - desired_bandwidth)
    cost_score = center["cost"]
    
    # Define a scoring function based on your priorities
    total_score = latency_score + bandwidth_score + cost_score
    
    if total_score < best_score and center["cost"] <= max_cost:
        best_data_center = center
        best_score = total_score
    power_consumption = best_data_center.get("power_consumption", 0)  # Replace with actual power consumption value
    carbon_emissions = best_data_center.get("carbon_emissions", 0)  # Replace with actual carbon emissions value
    water_usage = best_data_center.get("water_usage", 0)  # Replace with actual water usage value

    # IT power consumption (assumed to be 80% of total power consumption)
    it_power = 0.8 * power_consumption

    # Calculate PUE, CUE, and WUE
    pue = power_consumption / it_power
    cue = carbon_emissions / it_power
    wue = water_usage / it_power
    print("\nData Center Efficiency Metrics:")
    print(f"+------------+-------------------+")
    print(f"| Metric     | Value             |")
    print(f"+------------+-------------------+")
    print(f"| PUE        | {pue:.2f}              |")
    print(f"| CUE        | {cue:.2f}              |")
    print(f"| WUE        | {wue:.2f}              |")
    print(f"+------------+-------------------+")

# Output the best data center
if best_data_center:
    print("Best Data Center:")
    print(f"Name: {best_data_center['name']}")
    print(f"Latency to Metro: {best_data_center['latency_to_metro']} ms")
    print(f"Bandwidth: {best_data_center['bandwidth']} Gbps")
    print(f"Monthly Cost: ${best_data_center['cost']}")
    print(f"Total Score: {best_score}")

    # Calculate PUE, CUE, and WUE here
   

else:
    print("No suitable data center found within your criteria.")

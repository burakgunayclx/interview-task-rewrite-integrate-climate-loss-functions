import json
import math

# Load and parse the JSON data file
def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Calculate total projected loss using advanced mathematical operations
def calculate_projected_losses(building_data):
    total_loss = 0
    for building in building_data:
        floor_area = building['floor_area']
        construction_cost = building['construction_cost']
        hazard_probability = building['hazard_probability']
        inflation_rate = building['inflation_rate']
        resilience_factor = building['resilience_factor']

        # Calculate the present value of future construction costs adjusted for inflation
        future_cost = construction_cost * math.exp(inflation_rate * floor_area / 1000)

        # Calculate risk-adjusted loss using the probability of hazard occurrence and exponential decay based on resilience
        risk_adjusted_loss = future_cost * floor_area * (1 - math.exp(-hazard_probability * resilience_factor))

        # Apply a discount factor for present value calculation of future losses
        discount_rate = 0.05  # Assuming a 5% discount rate
        present_value_loss = risk_adjusted_loss / math.pow((1 + discount_rate), 1)  # Discounting for one year

        # Aggregate the total loss
        total_loss += present_value_loss

    return total_loss

# Calculate potential savings from mitigation measures
def calculate_savings(building_data):
    total_savings = 0
    for building in building_data:
        mitigation_effectiveness = building['mitigation_effectiveness']
        mitigation_cost = building['mitigation_cost']
        expected_lifetime = building['expected_lifetime']

        # Calculate savings as present value of mitigation effectiveness over expected lifetime, adjusted for mitigation cost
        annual_savings = mitigation_effectiveness * 1000 - mitigation_cost
        total_savings += math.fsum([annual_savings / math.pow((1 + 0.05), year) for year in range(1, expected_lifetime + 1)])

    return total_savings

# Main execution function
def main():
    data = load_data('data.json')
    total_projected_loss = calculate_projected_losses(data)
    total_savings = calculate_savings(data)
    print(f"Total Projected Loss: ${total_projected_loss:.2f}")
    print(f"Total Savings from Mitigation: ${total_savings:.2f}")

if __name__ == '__main__':
    main()

# Climate Hazard Loss Projection System

## Overview
This project includes a Python backend and a React frontend designed to calculate and display projected financial losses due to climate-related hazards for buildings. The backend handles complex financial calculations to estimate potential losses and savings from mitigation measures.

## Repository Setup
Before you begin, you will need to set up your own version of this repository:
- **Forking**: If you have GitHub access, please fork this repository to your own account. This action will create a personal copy that you can modify freely without affecting the original.
- **Cloning**: If you prefer to clone the repository directly:
  - Use the command `git clone https://github.com/climate-x-org/interview-task-rewrite-integrate-climate-loss-functions.git` to clone the repository after forking it to your account.

## Part 1: Python Backend Task - `losses_calculator.py`

### Description
The Python script `losses_calculator.py` is engineered to perform complex financial calculations to estimate potential losses from climate hazards. It uses inputs such as building area, construction costs, hazard probabilities, and economic factors like inflation and resilience to compute the projected losses and potential savings from mitigation measures.

### Variables Used
- **`floor_area`**: Total usable area of the building (in square meters).
- **`construction_cost`**: Cost per square meter for construction or repair.
- **`hazard_probability`**: Likelihood of experiencing a significant climate-related event.
- **`inflation_rate`**: Annual rate at which costs increase due to economic factors.
- **`resilience_factor`**: Building's resistance to damage from climate hazards.
- **`mitigation_effectiveness`**: Effectiveness of measures to reduce potential damages.
- **`mitigation_cost`**: Cost of implementing mitigation strategies per square meter.
- **`expected_lifetime`**: Expected duration that the mitigation measures will be effective.

### Backend Task Instructions
Candidates are expected to:
1. Review the script, identify and correct any inaccuracies in the calculations.
2. Optimize the code for performance and clarity.
3. Ensure the script aligns with the detailed variable descriptions and functional explanations provided.

### Objectives

The primary objective of the script is to:

Calculate the present value of projected losses due to climate hazards, considering factors like inflation, hazard probability, building resilience, and the time value of money.

### Detailed Variable Descriptions

- floor_area (building['floor_area']):
  - Represents the total usable surface area of the building measured in square metres. This variable is crucial as it directly influences the base calculation of potential losses, with larger areas generally leading to higher potential costs.

- construction_cost (building['construction_cost']):
  - Indicates the cost per square metre to build or repair the structure. This cost is utilised to estimate the raw financial impact before adjusting for other factors like hazard rates and inflation.

- hazard_probability (building['hazard_probability']):
  - A value representing the likelihood of a climate hazard occurring at the location of the building within a given year. This probability is used to adjust the financial impact based on the risk level associated with the location.

- inflation_rate (building['inflation_rate']):
  - The annual rate at which costs are expected to rise due to inflation. This rate is applied to adjust future costs to their present value, acknowledging that costs tend to increase over time due to economic factors.

- resilience_factor (building['resilience_factor']):
  - Measures the building's capability to withstand and mitigate the effects of the specified hazards. A higher resilience factor decreases the effective hazard impact, thereby potentially reducing the projected losses.

- mitigation_effectiveness (building['mitigation_effectiveness']):
  - Quantifies how effective mitigation strategies are in reducing potential damages. This effectiveness translates into savings by reducing the extent of damage expected during hazard events.

- mitigation_cost (building['mitigation_cost']):
  - The cost of implementing mitigation measures per square metre. While these costs contribute to upfront expenses, they are typically offset by the long-term savings due to reduced damage.

- expected_lifetime (building['expected_lifetime']):
  - The number of years for which the mitigation measures are expected to be effective. This duration is used to calculate the total value of future savings, discounting them back to their present value.

### Functional Explanation

The script operates in several steps:

1. Data Loading: First, it reads in building data from a JSON file. This data includes all the variables necessary for the calculations.
2. Loss Calculation: It calculates the initial losses based on construction costs and floor area, then adjusts these figures based on the hazard probability and the building's resilience.
3. Inflation Adjustment: Adjusts the estimated costs for inflation to reflect future values.
4. Risk Adjustment: Applies the hazard probability, adjusted for the building's resilience, to estimate risk-adjusted losses.
5. Discounting: Converts future values into present values using a discount rate, reflecting the principle that money available at the present time is worth more than the same amount in the future due to its potential earning capacity.

### Expected Output
The script outputs the total projected loss for all buildings, incorporating adjustments for inflation, hazard probability, resilience, and mitigation. It also computes total potential savings from implemented mitigation measures, providing a comprehensive financial assessment.

## Starting the Project
Once you have set up your local or forked repository:
1. Navigate to the directory where you cloned the repository.
2. Ensure Python is installed on your system, and install any dependencies if listed in `requirements.txt` by running `pip install -r requirements.txt`.
3. Run the script using a Python interpreter to see the output and begin testing or development.

### Note
Please ensure all your changes are committed to your fork or branch to maintain isolation from the main project repository. This setup helps preserve the integrity of the original project and provides a clear history of your modifications.

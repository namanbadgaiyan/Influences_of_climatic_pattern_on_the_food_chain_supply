# visualization.py
import matplotlib.pyplot as plt

# def visualize_results(predictions, actual):
#     # Create a new figure
#     plt.figure(figsize=(10, 6))

#     # Plot actual and predicted values
#     plt.plot(actual, label='Actual', marker='o')
#     plt.plot(predictions, label='Predicted', marker='x')

#     # Add labels and title
#     plt.xlabel('Sample')
#     plt.ylabel('Value')
#     plt.title('Comparison of Actual and Predicted Values')
    
#     # Add legend
#     plt.legend()

#     # Display the plot
#     plt.show()


# def visualize_feature_importances(model, feature_names):
#     # Get feature importances from the model
#     importances = model.feature_importances_
    
#     # Sort feature importances in descending order
#     indices = importances.argsort()[::-1]

#     # Plot feature importances
#     plt.figure(figsize=(10, 6))
#     plt.bar(range(len(indices)), importances[indices], align='center')
#     plt.xticks(range(len(indices)), [feature_names[i] for i in indices], rotation=45, ha='right')
#     plt.xlabel('Feature')
#     plt.ylabel('Feature Importance')
#     plt.title('Feature Importances')
#     plt.tight_layout()
#     plt.show()


# visualization.py
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def visualize_results(predictions, actual):
    # Create interactive plot using matplotlib and ipywidgets
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(actual, label='Actual', marker='o')
    ax.plot(predictions, label='Predicted', marker='x')
    ax.set_xlabel('Sample')
    ax.set_ylabel('Value')
    ax.set_title('Comparison of Actual and Predicted Values')
    ax.legend()
    
    # Create sliders to zoom and pan the plot
    zoom_slider = widgets.FloatSlider(value=1.0, min=0.1, max=2.0, step=0.1, description='Zoom:')
    pan_slider = widgets.FloatSlider(value=0.0, min=-10.0, max=10.0, step=1.0, description='Pan:')
    
    # Define update function to adjust plot based on slider values
    def update_plot(zoom, pan):
        ax.set_xlim(0, len(actual))
        ax.set_ylim(min(min(actual), min(predictions)), max(max(actual), max(predictions)))
        ax.set_xticks(range(0, len(actual), int(len(actual) / 10)))
        ax.set_xticklabels(range(0, len(actual), int(len(actual) / 10)))
        ax.set_xlim(pan, pan + len(actual) / zoom)
        plt.show()
    
    # Display sliders and connect them to update function
    widgets.interact(update_plot, zoom=zoom_slider, pan=pan_slider)
    plt.show()

def visualize_feature_importances(model, feature_names):
    # Create interactive bar plot using matplotlib and ipywidgets
    fig, ax = plt.subplots(figsize=(10, 6))
    importances = model.feature_importances_
    indices = importances.argsort()[::-1]
    ax.bar(range(len(indices)), importances[indices], align='center')
    ax.set_xticks(range(len(indices)))
    ax.set_xticklabels([feature_names[i] for i in indices], rotation=45, ha='right')
    ax.set_xlabel('Feature')
    ax.set_ylabel('Feature Importance')
    ax.set_title('Feature Importances')
    plt.tight_layout()
    plt.show()

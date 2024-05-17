# main.py
from data_preprocessing import preprocess_data
from data_analysis import analyze_data
from modeling import train_model
from visualization import visualize_results
from visualization import visualize_feature_importances

def main():
    # Step 1: Data Preprocessing
    print("Step 1: Data Preprocessing...")
    climatic_file = "data/climatic_data.csv"
    food_file = "data/food_data.csv"
    preprocessed_data = preprocess_data(climatic_file, food_file)
    
    # Step 2: Data Analysis
    print("Step 2: Data Analysis...")
    analysis_results = analyze_data(preprocessed_data)
    print(analysis_results)
    
    # Step 3: Modeling
    print("Step 3: Modeling...")
    X = preprocessed_data.drop(columns=['crop_yield'])  # Dropping the target column
    y = preprocessed_data['crop_yield']
    model = train_model(X, y)
    
    # Step 4: Visualization
    print("Step 4: Visualization...")
    predictions = model.predict(X)  # Or use a separate test dataset
    visualize_results(predictions, y)  # Pass actual target values instead of 'actual'
    visualize_feature_importances(model, X.columns)

if __name__ == "__main__":
    main()

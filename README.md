# README: Dataset Finder

## Overview

The **Dataset Finder** is a Streamlit app that helps users search for datasets online by entering a topic of interest. The app uses the `googlesearch` library to perform a Google search for datasets related to the entered topic, and then presents the search results in a simple table format. This tool is helpful for researchers, students, or anyone looking to find relevant datasets for their projects or studies.
I created this project so that its easier for me to find datasets and literature surveys easier for research.
### Key Features:
- **Search for Datasets by Topic:** Users can input a topic, and the app will search for datasets related to that topic.
- **Display Search Results:** The app shows the results of the Google search, listing links to datasets.
- **Simple, User-Friendly Interface:** The app is easy to use with minimal setup, allowing users to quickly find datasets.

## Requirements

Before running the project, ensure that the following Python libraries are installed:
- `streamlit` – for creating the web interface.
- `googlesearch-python` – for performing Google searches.
- `pandas` – for organizing and displaying the search results.

You can install the required libraries by running:

```bash
pip install streamlit googlesearch-python pandas
```

## Usage

### 1. **Run the Streamlit App:**

To start the Streamlit app, open a terminal and run the following command:

```bash
streamlit run app.py
```

Replace `app.py` with the filename if you saved it with a different name.

### 2. **Search for Datasets:**

- Enter a topic in the input field (e.g., "climate change," "financial data," "machine learning datasets").
- The app will search for datasets related to your topic on Google.

### 3. **View the Results:**

- The search results will be displayed in a table with clickable links to dataset sources.
- If no results are found, the app will display a message indicating no datasets were found for your topic.

### 4. **Error Handling:**

- If an error occurs during the search process, such as a network issue or invalid query, the app will display an error message explaining the problem.

## Code Breakdown

### Topic Input:
The app uses Streamlit’s `text_input` widget to prompt the user to enter a topic for searching datasets.

### Google Search:
The `googlesearch` library performs a search query for datasets related to the entered topic. The query is dynamically constructed as `dataset {topic}`, where `{topic}` is replaced by the user’s input.

### Displaying Results:
The search results (links) are collected in a list, which is then converted into a pandas DataFrame. This DataFrame is displayed as an HTML table in the app.

### Error Handling:
If the search fails or no results are found, appropriate error or message handling is shown to the user.

## Example Usage

### Enter Topic:

- Example input: `"climate change datasets"`

### Display Results:

The app will display a list of links to datasets related to "climate change," such as links to government websites, academic datasets, or repositories like Kaggle.

| Link |
|------|
| [Dataset 1](https://example.com/dataset1) |
| [Dataset 2](https://example.com/dataset2) |
| [Dataset 3](https://example.com/dataset3) |

## Contributing

If you’d like to contribute to the development of this app, feel free to open issues or submit pull requests. Any improvements, bug fixes, or feature suggestions are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This app uses Google Search to find datasets. The results are based on the available search results and may vary depending on the topic and current search index. Ensure that any datasets you access comply with your local data usage policies.

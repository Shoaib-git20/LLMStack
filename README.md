# LMMsStack: Memory Efficient Inference and Dynamic Contrastive Reasoning in Financial Decision Making?

### Setting Up the Virtual Environment

1. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    ```

2. **Activate the virtual environment**:
    - **Windows Command Prompt**:
        ```sh
        .venv\Scripts\activate.bat
        ```
    - **Windows PowerShell**:
        ```sh
        .venv\Scripts\Activate.ps1
        ```
    - **macOS and Linux**:
        ```sh
        source .venv/bin/activate
        ```

### Installing Dependencies

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

### code files structure

4. **data**:
    ```sh
    |-data
     --img_data
        --test
    
    |-chartqa.ipynb (vision model)
    |-headlines.ipynb (price predtiction model)
    |-math.ipynb (math model)
    |-normal.ipynb (general model that uses Qwen 7B for all queries)
    ```

Now your application should be running locally! If you encounter any issues, make sure all dependencies are correctly installed and the virtual environment is activated.

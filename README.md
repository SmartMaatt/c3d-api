<h1 align="center">c3d api</h1>

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#components">Components</a> •
  <a href="#installation">Installation</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/badge/Authors-Devision303-red" />
</p>


## Introduction
The `c3d-api` repository is dedicated to motion capture data processing, particularly focused on `.c3d` file interpretation, conversion of data formats, and preparation of datasets for machine learning applications. It features three main Python-based CLI applications, each addressing a specific aspect of motion capture data manipulation.


## Components
### 1. C3D File Interpreter
The C3D File Interpreter is a key component designed to extract and process data from `.c3d` files used in motion capture systems. This tool focuses on:

- **Data Extraction:** Parsing the three segments (header, parameters, and data) of `.c3d` files to access motion capture data.
- **Selective Data Export:** Enabling users to choose specific data sections (markers, virtual markers, modeled markers, angles, forces, moments, and power) for export.
- **CSV Output:** Converting and saving the selected data to `.csv` format for ease of use in applications like Microsoft Excel.
- **Specialized for Joint Angles:** Primarily used for exporting joint angles as Cardan angles, facilitating detailed motion analysis.

### 2. Cardan Angles to Quaternions Converter
This application bridges the gap between traditional angle representations and modern quaternion-based methods used in advanced motion analysis and machine learning:

- **Cardan to Quaternion Conversion:** Transforms Cardan angles from `.csv` files into quaternion sequences, a more robust representation for 3D rotations.
- **Utilization of Scipy Library:** Leverages Scipy's scientific computing capabilities for accurate and efficient conversion processes.
- **Structured Output:** Produces a `.csv` file mirroring the structure of the input but with quaternion data, ensuring compatibility with subsequent processing stages.

### 3. Training Dataset Generator
A crucial tool for preparing machine learning datasets from motion capture data:

- **Dataset Preparation:** Generates training and validation datasets tailored for use in recurrent neural network models.
- **Flexible Data Handling:** Capable of processing output from both the C3D interpreter and the quaternion converter.
- **Customizable Sequence Length:** Allows users to define the sequence length `n`, essential for configuring datasets for specific machine learning models.
- **Output Files:** Creates two `.csv` files – one for training and another for validation, formatted for direct use in neural network training environments.


## Installation
1. Create a Conda Environment:
   ```
   conda env create -f environment.yaml
   ```

2. **Setup the Development Environment:**
   Open the "app" folder in Visual Studio Code.

3. **Activate the Python Interpreter:**
   Use the command palette in VSCode (Ctrl + Shift + P) and select `Python: Select Interpreter`. Choose the `c3d_api` environment.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
&copy; 2023 Devision303. All rights reserved.
<a href="https://devision303.pl/">
    <img src="https://smartmatt.pl/github/devision-logo.png" title="Devision Logo" align="right" width="60" />
</a>

<p align="left">
  <a href="https://devision303.pl/">Website</a> •
  <a href="https://www.facebook.com/Dywizjon303Polakposting">Facebook</a>
</p>

<p align="left">
  Igor Budzyński (Multiprice):
  <a href="https://github.com/MultiPrice">GitHub</a> •
  <a href="https://www.linkedin.com/in/igor-budzy%C5%84ski-48b650214/">LinkedIn</a>
</p>

<p align="left">
  Krzysztof Kocot (Pocot997):
  <a href="https://github.com/pocot997">GitHub</a> •
  <a href="https://www.linkedin.com/in/%CC%B6m%CC%B6g%CC%B6r%CC%B6-in%C5%BC-krzysztof-kocot-9b0b62140/">LinkedIn</a>
</p>

<p align="left">
  Mateusz Płonka (SmartMatt):
  <a href="https://smartmatt.pl/">Portfolio</a> •
  <a href="https://github.com/SmartMaatt">GitHub</a> •
  <a href="https://www.linkedin.com/in/mateusz-p%C5%82onka-328a48214/">LinkedIn</a> •
  <a href="https://www.youtube.com/user/SmartHDesigner">YouTube</a> •
  <a href="https://www.tiktok.com/@smartmaatt">TikTok</a>
</p>

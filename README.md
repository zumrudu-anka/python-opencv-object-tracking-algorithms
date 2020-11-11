# 🕵️‍♂️ Object Tracking Algorithms with OpenCV

1. **[BOOSTING](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/1.BOOSTING)**
2. **[MIL](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/2.MIL)**
3. **[KCF](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/3.KCF)**
4. **[TLD](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/4.TLD)**
5. **[MEDIANFLOW](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/5.MEDIANFLOW)**
6. **[GOTURN](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/6.GOTURN)**
7. **[MOSSE](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/7.MOSSE)**
8. **[CSRT](https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/ALGORITHMS/8.CSRT)**

### Running Sample With KCF

<p align="center">
    <table align="center">
        <tr>
            <th>Input</th>
            <th>Output</th>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/resources/gifs/input.gif">
            </td>
            <td>
                <img src="https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms/blob/main/resources/gifs/output.gif">
            </td>
        </tr>
    </table>
</p>

### Installation

- Clone the repo to your local machine `git clone https://github.com/zumrudu-anka/python-opencv-object-tracking-algorithms.git`
- Go to the project folder
- Run `python -m venv venv` for create virtual environment which name is venv
- Activate the virtual environment:
  > For Windows:
  > - Run `venv\Scripts\activate`

  > For Linux:
  > - Run `source venv/bin/activate`
- Run `pip install -r requirements`
- Download and extract `goturn.caffemodel` and `goturn.prototxt` files from this [link](https://github.com/opencv/opencv_extra/tree/c4219d5eb3105ed8e634278fad312a1a8d2c182d/testdata/tracking) for run GOTURN Algorithm.
- Put these files in to the project directory.

### Usage

- run `python main.py`
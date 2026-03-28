# Compound Class Visual Representation

A Python script that generates a binary heatmap showing the presence or absence of compound classes across biofuel sample categories, based on FTIR spectral assignments.

---

## Author

**Nitish Kapur**<br>
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)

---

## Overview

Each row of the heatmap represents a compound class (e.g. Alkanes, Aromatics) and each column represents a sample category (e.g. WL, Diesel, Ethanol). A green cell indicates the compound class is present in that sample category; a red cell indicates absence.

---

## Sample Categories

| Symbol | Description |
|---|---|
| `WL` | Waterless liquid |
| `D SUM` | Waterless liquid densified at ~30 °C (summer) |
| `D WIN` | Waterless liquid densified at ~15 °C (winter onset) |
| `W` | Wax |
| `WW` | Wax with possible water content |
| `DW` | Water-containing liquid densified at ~30 °C (summer) |
| `OH` | Flammable liquid with possible water content |
| `Diesel` | Reference fuel |
| `Kerosene` | Reference fuel |
| `E20 Petrol` | Reference fuel |
| `Ethanol` | Reference alcohol |

---

## Requirements
```bash
pip install pandas numpy matplotlib
```

---

## Usage

Run the script directly:
```bash
python binary-matrix-compound-class.py
```

The heatmap will be displayed interactively and saved as `binaryMatrixRedGreen_.png` in the working directory.

---

## Output

- `binaryMatrixRedGreen_.png` — binary heatmap saved in the working directory
- X-axis: Sample categories (alphabetically ordered)
- Y-axis: Compound classes (alphabetically ordered)
- Green: compound class present in that sample category
- Red: compound class absent in that sample category

---

## Notes

- The compound class assignments and sample category mappings are hard-coded in the script. Edit the `mapping` and `compound_classes` dictionaries to update them.
- To change the category display order, edit the `custom_order` list.

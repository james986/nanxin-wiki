# SM1401PSS

<div style="margin-top: -0.75rem; margin-bottom: 0.75rem; color: var(--fs-content-fg); font-size: 1.08rem; font-weight: 500; line-height: 1.45; opacity: 0.78;">
P-Channel Enhancement Mode MOSFET
</div>

{{ pdf_line("../pdf/SM1401PSSC_Datasheet.pdf", "下载规格书", "48px") }}

<!--
MOSFET datasheet template notes:
1. Keep every visible datasheet section title as a Markdown "##" heading.
2. Do not promote table column names or table-internal field names to page headings.
3. Keep table grouping rows inside the table when they belong to a table, for example Static Characteristics under Electrical Characteristics.
4. Use extracted images for diagrams, curves, waveforms, and profile graphics.
-->

## Features

- -20V/-3.7A,<br>
  <span style="display: inline-block; margin-left: 1.5rem;">R<sub>DS(ON)</sub> = 78mΩ (Max.) @ V<sub>GS</sub> = -4.5V</span><br>
  <span style="display: inline-block; margin-left: 1.5rem;">R<sub>DS(ON)</sub> = 115mΩ (Max.) @ V<sub>GS</sub> = -2.5V</span><br>
  <span style="display: inline-block; margin-left: 1.5rem;">R<sub>DS(ON)</sub> = 165mΩ (Max.) @ V<sub>GS</sub> = -1.8V</span>
- Super High Dense Cell Design
- Reliable and Rugged
- Lead Free and Green Devices Available (RoHS Compliant)

## Applications

- Power Management in Notebook Computer, Portable Equipment and Battery Powered Systems.

## Pin Description

<div style="display: flex; gap: 1.25rem; align-items: flex-start; margin: 0.5rem 0 1rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <img src="../images/sm1401pssc-top-view-of-sc-70.png" alt="Top View of SC-70" style="width: 100%; max-width: 360px; height: auto; margin: 0 auto; padding: 0; border: none; box-shadow: none;">
    <div style="font-weight: 700; margin-top: 0.35rem;">Top View of SC-70</div>
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <img src="../images/sm1401pssc-p-channel-mosfet.png" alt="P-Channel MOSFET" style="width: 100%; max-width: 360px; height: auto; margin: 0 auto; padding: 0; border: none; box-shadow: none;">
    <div style="font-weight: 700; margin-top: 0.35rem;">P-Channel MOSFET</div>
  </div>
</div>

## Ordering and Marking Information

<img src="../images/sm1401pssc-ordering-and-marking-information.png" alt="Ordering and Marking Information" style="width: 100%; max-width: 940px; height: auto; display: block; margin: 0 auto 0.5rem;">

!!! note "Note"

    SINOPOWER lead-free products contain molding compounds/die attach materials and 100% matte tin plate termination finish; which are fully compliant with RoHS. SINOPOWER lead-free products meet or exceed the lead-free requirements of IPC/JEDEC J-STD-020D for MSL classification at lead-free peak reflow temperature. SINOPOWER defines “Green” to mean lead-free (RoHS compliant) and halogen free (Br or Cl does not exceed 900ppm by weight in homogeneous material and total of Br and Cl does not exceed 1500ppm by weight).

SINOPOWER reserves the right to make changes to improve reliability or manufacturability without notice, and advise customers to obtain the latest version of relevant information to verify before placing orders.

## Absolute Maximum Ratings

(T<sub>A</sub> = 25°C unless otherwise noted)

<table>
  <tr>
    <th align="left">Symbol</th>
    <th align="left">Parameter</th>
    <th align="left">Conditions</th>
    <th align="left">Rating</th>
    <th align="left">Unit</th>
  </tr>
  <tr>
    <td>V<sub>DSS</sub></td>
    <td>Drain-Source Voltage</td>
    <td>-</td>
    <td>-20</td>
    <td>V</td>
  </tr>
  <tr>
    <td>V<sub>GSS</sub></td>
    <td>Gate-Source Voltage</td>
    <td>-</td>
    <td>±12</td>
    <td>V</td>
  </tr>
  <tr>
    <td>T<sub>J</sub></td>
    <td>Maximum Junction Temperature</td>
    <td>-</td>
    <td>150</td>
    <td>°C</td>
  </tr>
  <tr>
    <td>T<sub>STG</sub></td>
    <td>Storage Temperature Range</td>
    <td>-</td>
    <td>-55 to 150</td>
    <td>°C</td>
  </tr>
  <tr>
    <td>I<sub>S</sub></td>
    <td>Diode Continuous Forward Current</td>
    <td>-</td>
    <td>-1</td>
    <td>A</td>
  </tr>
  <tr>
    <td rowspan="2">I<sub>D</sub><sup>a</sup></td>
    <td rowspan="2">Continuous Drain Current</td>
    <td>T<sub>A</sub> = 25°C</td>
    <td>-3.3</td>
    <td rowspan="4">A</td>
  </tr>
  <tr>
    <td>T<sub>A</sub> = 70°C</td>
    <td>-2.5</td>
  </tr>
  <tr>
    <td rowspan="2">I<sub>DM</sub><sup>b</sup></td>
    <td rowspan="2">Pulsed Drain Current</td>
    <td>T<sub>A</sub> = 25°C</td>
    <td>-13.2</td>
  </tr>
  <tr>
    <td>T<sub>A</sub> = 70°C</td>
    <td>-10</td>
  </tr>
  <tr>
    <td rowspan="2">P<sub>D</sub><sup>a</sup></td>
    <td rowspan="2">Maximum Power Dissipation</td>
    <td>T<sub>A</sub> = 25°C</td>
    <td>1.1</td>
    <td rowspan="2">W</td>
  </tr>
  <tr>
    <td>T<sub>A</sub> = 70°C</td>
    <td>0.7</td>
  </tr>
  <tr>
    <td rowspan="2">R<sub>θJA</sub><sup>c</sup></td>
    <td rowspan="2">Thermal Resistance-Junction to Ambient</td>
    <td>t ≤ 10s</td>
    <td>115</td>
    <td rowspan="2">°C/W</td>
  </tr>
  <tr>
    <td>Steady state</td>
    <td>160</td>
  </tr>
</table>

!!! note "Note"

    a. Surface mounted on 1in² pad area, t ≤ 10s.  
    b. Pulse width is limited by max. junction temperature.  
    c. Surface mounted on 1in² pad area, Steady State = 999s.

## Electrical Characteristics

(T<sub>A</sub> = 25°C unless otherwise noted)

<table>
  <tr>
    <th align="left">Symbol</th>
    <th align="left">Parameter</th>
    <th align="left">Test Conditions</th>
    <th align="left">Min.</th>
    <th align="left">Typ.</th>
    <th align="left">Max.</th>
    <th align="left">Unit</th>
  </tr>
  <tr>
    <th colspan="7" align="left">Static Characteristics</th>
  </tr>
  <tr>
    <td>B<sub>VDSS</sub></td>
    <td>Drain-Source Breakdown Voltage</td>
    <td>V<sub>GS</sub> = 0V, I<sub>DS</sub> = -250µA</td>
    <td>-20</td>
    <td>-</td>
    <td>-</td>
    <td>V</td>
  </tr>
  <tr>
    <td rowspan="2">I<sub>DSS</sub></td>
    <td rowspan="2">Zero Gate Voltage Drain Current</td>
    <td>V<sub>DS</sub> = -16V, V<sub>GS</sub> = 0V</td>
    <td>-</td>
    <td>-</td>
    <td>-1</td>
    <td rowspan="2">µA</td>
  </tr>
  <tr>
    <td>T<sub>J</sub> = 85°C</td>
    <td>-</td>
    <td>-</td>
    <td>-30</td>
  </tr>
  <tr>
    <td>V<sub>GS(th)</sub></td>
    <td>Gate Threshold Voltage</td>
    <td>V<sub>DS</sub> = V<sub>GS</sub>, I<sub>DS</sub> = -250µA</td>
    <td>-0.5</td>
    <td>-0.75</td>
    <td>-1</td>
    <td>V</td>
  </tr>
  <tr>
    <td>I<sub>GSS</sub></td>
    <td>Gate Leakage Current</td>
    <td>V<sub>GS</sub> = ±10V, V<sub>DS</sub> = 0V</td>
    <td>-</td>
    <td>-</td>
    <td>±10</td>
    <td>µA</td>
  </tr>
  <tr>
    <td rowspan="4">R<sub>DS(ON)</sub><sup>d</sup></td>
    <td rowspan="4">Drain-Source On-State Resistance</td>
    <td>V<sub>GS</sub> = -4.5V, I<sub>DS</sub> = -2.8A</td>
    <td>-</td>
    <td>62</td>
    <td>78</td>
    <td rowspan="4">mΩ</td>
  </tr>
  <tr>
    <td>T<sub>J</sub> = 125°C</td>
    <td>-</td>
    <td>85</td>
    <td>-</td>
  </tr>
  <tr>
    <td>V<sub>GS</sub> = -2.5V, I<sub>DS</sub> = -1.8A</td>
    <td>-</td>
    <td>85</td>
    <td>115</td>
  </tr>
  <tr>
    <td>V<sub>GS</sub> = -1.8V, I<sub>DS</sub> = -0.5A</td>
    <td>-</td>
    <td>110</td>
    <td>165</td>
  </tr>
  <tr>
    <th colspan="7" align="left">Diode Characteristics<sup>e</sup></th>
  </tr>
  <tr>
    <td>V<sub>SD</sub><sup>d</sup></td>
    <td>Diode Forward Voltage</td>
    <td>I<sub>SD</sub> = -1A, V<sub>GS</sub> = 0V</td>
    <td>-</td>
    <td>-0.7</td>
    <td>-1</td>
    <td>V</td>
  </tr>
  <tr>
    <td>t<sub>rr</sub></td>
    <td>Reverse Recovery Time</td>
    <td rowspan="4">I<sub>SD</sub> = -3.3A, dI<sub>SD</sub>/dt = 100A/µs</td>
    <td>-</td>
    <td>20</td>
    <td>-</td>
    <td rowspan="3">ns</td>
  </tr>
  <tr>
    <td>t<sub>a</sub></td>
    <td>Charge Time</td>
    <td>-</td>
    <td>5</td>
    <td>-</td>
  </tr>
  <tr>
    <td>t<sub>b</sub></td>
    <td>Discharge Time</td>
    <td>-</td>
    <td>16</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Q<sub>rr</sub></td>
    <td>Reverse Recovery Charge</td>
    <td>-</td>
    <td>6</td>
    <td>-</td>
    <td>nC</td>
  </tr>
  <tr>
    <th colspan="7" align="left">Dynamic Characteristics<sup>e</sup></th>
  </tr>
  <tr>
    <td>R<sub>G</sub></td>
    <td>Gate Resistance</td>
    <td>V<sub>GS</sub> = 0V, V<sub>DS</sub> = 0V, F = 1MHz</td>
    <td>-</td>
    <td>10</td>
    <td>20</td>
    <td>Ω</td>
  </tr>
  <tr>
    <td>C<sub>iss</sub></td>
    <td>Input Capacitance</td>
    <td rowspan="3">V<sub>GS</sub> = 0V, V<sub>DS</sub> = -10V, Frequency = 1.0MHz</td>
    <td>-</td>
    <td>360</td>
    <td>468</td>
    <td rowspan="3">pF</td>
  </tr>
  <tr>
    <td>C<sub>oss</sub></td>
    <td>Output Capacitance</td>
    <td>-</td>
    <td>84</td>
    <td>-</td>
  </tr>
  <tr>
    <td>C<sub>rss</sub></td>
    <td>Reverse Transfer Capacitance</td>
    <td>-</td>
    <td>70</td>
    <td>-</td>
  </tr>
  <tr>
    <td>t<sub>d(ON)</sub></td>
    <td>Turn-on Delay Time</td>
    <td rowspan="4">V<sub>DD</sub> = -10V, R<sub>L</sub> = 10Ω, I<sub>DS</sub> = -1A, V<sub>GEN</sub> = -4.5V, R<sub>G</sub> = 6Ω</td>
    <td>-</td>
    <td>7</td>
    <td>-</td>
    <td rowspan="4">ns</td>
  </tr>
  <tr>
    <td>t<sub>r</sub></td>
    <td>Turn-on Rise Time</td>
    <td>-</td>
    <td>13.6</td>
    <td>-</td>
  </tr>
  <tr>
    <td>t<sub>d(OFF)</sub></td>
    <td>Turn-off Delay Time</td>
    <td>-</td>
    <td>27</td>
    <td>-</td>
  </tr>
  <tr>
    <td>t<sub>f</sub></td>
    <td>Turn-off Fall Time</td>
    <td>-</td>
    <td>26</td>
    <td>-</td>
  </tr>
  <tr>
    <th colspan="7" align="left">Gate Charge Characteristics<sup>e</sup></th>
  </tr>
  <tr>
    <td>Q<sub>g</sub></td>
    <td>Total Gate Charge</td>
    <td rowspan="4">V<sub>DS</sub> = -10V, V<sub>GS</sub> = -4.5V, I<sub>DS</sub> = -3.3A</td>
    <td>-</td>
    <td>4.7</td>
    <td>-</td>
    <td rowspan="4">nC</td>
  </tr>
  <tr>
    <td>Q<sub>gth</sub></td>
    <td>Threshold Gate Charge</td>
    <td>-</td>
    <td>0.3</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Q<sub>gs</sub></td>
    <td>Gate-Source Charge</td>
    <td>-</td>
    <td>0.6</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Q<sub>gd</sub></td>
    <td>Gate-Drain Charge</td>
    <td>-</td>
    <td>1.7</td>
    <td>-</td>
  </tr>
</table>

!!! note "Note"

    d. Pulse test; pulse width ≤ 300µs, duty cycle ≤ 2%.  
    e. Guaranteed by design, not subject to production testing.

## Typical Operating Characteristics

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Power Dissipation</div>
    <img src="../images/sm1401pssc-power-dissipation.png" alt="Power Dissipation" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Drain Current</div>
    <img src="../images/sm1401pssc-drain-current.png" alt="Drain Current" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Safe Operation Area</div>
    <img src="../images/sm1401pssc-safe-operation-area.png" alt="Safe Operation Area" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Thermal Transient Impedance</div>
    <img src="../images/sm1401pssc-thermal-transient-impedance.png" alt="Thermal Transient Impedance" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Output Characteristics</div>
    <img src="../images/sm1401pssc-output-characteristics.png" alt="Output Characteristics" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Drain-Source On Resistance</div>
    <img src="../images/sm1401pssc-drain-source-on-resistance-current.png" alt="Drain-Source On Resistance" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Gate-Source On Resistance</div>
    <img src="../images/sm1401pssc-gate-source-on-resistance.png" alt="Gate-Source On Resistance" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Gate Threshold Voltage</div>
    <img src="../images/sm1401pssc-gate-threshold-voltage.png" alt="Gate Threshold Voltage" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Drain-Source On Resistance</div>
    <img src="../images/sm1401pssc-drain-source-on-resistance-temperature.png" alt="Drain-Source On Resistance" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Source-Drain Diode Forward</div>
    <img src="../images/sm1401pssc-source-drain-diode-forward.png" alt="Source-Drain Diode Forward" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

<div style="display: flex; gap: 1.25rem; align-items: flex-start; width: calc(100% + 4rem); max-width: calc(100vw - 2rem); margin: 0.5rem 0 1rem -2rem;">
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Capacitance</div>
    <img src="../images/sm1401pssc-capacitance.png" alt="Capacitance" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
  <div style="width: calc(50% - 0.625rem); text-align: center;">
    <div style="font-weight: 700; margin-bottom: 0.35rem;">Gate Charge</div>
    <img src="../images/sm1401pssc-gate-charge.png" alt="Gate Charge" style="width: 100%; max-width: none; height: auto; margin: 0; padding: 0; border: none; box-shadow: none;">
  </div>
</div>

## Avalanche Test Circuit and Waveforms

<img src="../images/sm1401pssc-avalanche-test-circuit-and-waveforms.png" alt="Avalanche Test Circuit and Waveforms" style="width: 100%; max-width: 940px; height: auto; display: block; margin: 0 auto 0.5rem;">

## Switching Time Test Circuit and Waveforms

<img src="../images/sm1401pssc-switching-time-test-circuit-and-waveforms.png" alt="Switching Time Test Circuit and Waveforms" style="width: 100%; max-width: 940px; height: auto; display: block; margin: 0 auto 0.5rem;">

## Package Information

<img src="../images/sm1401pssc-sc70-package-outline.png" alt="SC-70 Package Outline" style="width: 100%; max-width: 940px; height: auto; display: block; margin: 0 auto 0.5rem;">

<table>
  <tr>
    <th rowspan="3" align="center">Symbol</th>
    <th colspan="4" align="center">SC-70</th>
  </tr>
  <tr>
    <th colspan="2" align="center">Millimeters</th>
    <th colspan="2" align="center">Inches</th>
  </tr>
  <tr>
    <th align="center">Min.</th>
    <th align="center">Max.</th>
    <th align="center">Min.</th>
    <th align="center">Max.</th>
  </tr>
  <tr>
    <td>A</td>
    <td>0.80</td>
    <td>1.10</td>
    <td>0.031</td>
    <td>0.043</td>
  </tr>
  <tr>
    <td>A1</td>
    <td>0.00</td>
    <td>0.10</td>
    <td>0.000</td>
    <td>0.004</td>
  </tr>
  <tr>
    <td>A2</td>
    <td>0.80</td>
    <td>1.00</td>
    <td>0.031</td>
    <td>0.040</td>
  </tr>
  <tr>
    <td>b</td>
    <td>0.20</td>
    <td>0.40</td>
    <td>0.008</td>
    <td>0.016</td>
  </tr>
  <tr>
    <td>c</td>
    <td>0.08</td>
    <td>0.25</td>
    <td>0.003</td>
    <td>0.010</td>
  </tr>
  <tr>
    <td>D</td>
    <td>1.90</td>
    <td>2.20</td>
    <td>0.075</td>
    <td>0.087</td>
  </tr>
  <tr>
    <td>E</td>
    <td>2.00</td>
    <td>2.40</td>
    <td>0.079</td>
    <td>0.095</td>
  </tr>
  <tr>
    <td>E1</td>
    <td>1.15</td>
    <td>1.35</td>
    <td>0.045</td>
    <td>0.053</td>
  </tr>
  <tr>
    <td>e</td>
    <td colspan="2" align="center">0.65 BSC</td>
    <td colspan="2" align="center">0.026 BSC</td>
  </tr>
  <tr>
    <td>e1</td>
    <td colspan="2" align="center">1.30 BSC</td>
    <td colspan="2" align="center">0.051 BSC</td>
  </tr>
  <tr>
    <td>L</td>
    <td>0.15</td>
    <td>0.45</td>
    <td>0.006</td>
    <td>0.018</td>
  </tr>
  <tr>
    <td>θ</td>
    <td>0°</td>
    <td>8°</td>
    <td>0°</td>
    <td>8°</td>
  </tr>
</table>

!!! note "Note"

    1. Followed from JEDEC MO-223.  
    2. Dimension D and E1 do not include mold flash, protrusions or gate burrs. Mold flash, protrusion or gate burrs shall not exceed 6 mil per side.

**RECOMMENDED LAND PATTERN**

<img src="../images/sm1401pssc-sc70-recommended-land-pattern.png" alt="Recommended Land Pattern" style="width: 100%; max-width: 280px; height: auto; display: block; margin: 0 auto 0.5rem;">

## Disclaimer

Sinopower Semiconductor Inc. (hereinafter “Sinopower”) has been making great efforts to development high quality and better performance products to satisfy all customers’ needs. However, a product may fail to meet customer’s expectation or malfunction for various situations.

All information which is shown in the datasheet is based on Sinopower’s research and development result, therefore, Sinopower shall reserve the right to adjust the content and monitor the production.

In order to unify the quality and performance, Sinopower has been following JEDEC while defines assembly rule. Notwithstanding all the suppliers basically follow the rule for each product, different processes may cause slightly different results.

The technical information specified herein is intended only to show the typical functions of and examples of application circuits for the products. Sinopower does not grant customers explicitly or implicitly, any license to use or exercise intellectual property or other rights held by Sinopower and other parties. Sinopower shall bear no responsible whatsoever for any dispute arising from the use of such technical information.

The products are not designed or manufactured to be used with any equipment, device or system which requires an extremely high level of reliability, such as the failure or malfunction of which any may result in a direct threat to human life or a risk of human injury. Sinopower shall bear no responsibility in any way for use of any of the products for the above special purposes. If a product is intended to use for any such special purpose, such as vehicle, military, or medical controller relevant applications, please contact Sinopower sales representative before purchasing.

## Classification Profile

<img src="../images/sm1401pssc-classification-profile.png" alt="Classification Profile" style="width: 100%; max-width: 940px; height: auto; display: block; margin: 0 auto 0.5rem;">

## Classification Reflow Profiles

<table>
  <tr>
    <th align="left">Profile Feature</th>
    <th align="left">Sn-Pb Eutectic Assembly</th>
    <th align="left">Pb-Free Assembly</th>
  </tr>
  <tr>
    <td>Preheat &amp; Soak Temperature min (T<sub>smin</sub>)</td>
    <td>100 °C</td>
    <td>150 °C</td>
  </tr>
  <tr>
    <td>Preheat &amp; Soak Temperature max (T<sub>smax</sub>)</td>
    <td>150 °C</td>
    <td>200 °C</td>
  </tr>
  <tr>
    <td>Time (T<sub>smin</sub> to T<sub>smax</sub>) (t<sub>s</sub>)</td>
    <td>60-120 seconds</td>
    <td>60-120 seconds</td>
  </tr>
  <tr>
    <td>Average ramp-up rate (T<sub>smax</sub> to T<sub>P</sub>)</td>
    <td>3 °C/second max.</td>
    <td>3 °C/second max.</td>
  </tr>
  <tr>
    <td>Liquidous temperature (T<sub>L</sub>)</td>
    <td>183 °C</td>
    <td>217 °C</td>
  </tr>
  <tr>
    <td>Time at liquidous (t<sub>L</sub>)</td>
    <td>60-150 seconds</td>
    <td>60-150 seconds</td>
  </tr>
  <tr>
    <td>Peak package body Temperature (T<sub>p</sub>)</td>
    <td>See Classification Temp in table 1</td>
    <td>See Classification Temp in table 2</td>
  </tr>
  <tr>
    <td>Time (t<sub>P</sub>) within 5 °C of the specified classification temperature (T<sub>C</sub>)</td>
    <td>20 seconds</td>
    <td>30 seconds</td>
  </tr>
  <tr>
    <td>Average ramp-down rate (T<sub>p</sub> to T<sub>smax</sub>)</td>
    <td>6 °C/second max.</td>
    <td>6 °C/second max.</td>
  </tr>
  <tr>
    <td>Time 25 °C to peak temperature</td>
    <td>6 minutes max.</td>
    <td>8 minutes max.</td>
  </tr>
</table>

!!! note "Note"

    *. Tolerance for peak profile Temperature (T<sub>p</sub>) is defined as a supplier minimum and a user maximum.  
    **. Tolerance for time at peak profile temperature (t<sub>p</sub>) is defined as a supplier minimum and a user maximum.

<table>
  <tr>
    <th colspan="3" align="left">Table 1. SnPb Eutectic Process - Classification Temperatures (T<sub>C</sub>)</th>
  </tr>
  <tr>
    <th align="left">Package Thickness</th>
    <th align="left">Volume mm³ &lt; 350</th>
    <th align="left">Volume mm³ ≥ 350</th>
  </tr>
  <tr>
    <td>&lt; 2.5 mm</td>
    <td>235 °C</td>
    <td>220 °C</td>
  </tr>
  <tr>
    <td>≥ 2.5 mm</td>
    <td>220 °C</td>
    <td>220 °C</td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="4" align="left">Table 2. Pb-free Process - Classification Temperatures (T<sub>C</sub>)</th>
  </tr>
  <tr>
    <th align="left">Package Thickness</th>
    <th align="left">Volume mm³ &lt; 350</th>
    <th align="left">Volume mm³ 350-2000</th>
    <th align="left">Volume mm³ &gt; 2000</th>
  </tr>
  <tr>
    <td>&lt; 1.6 mm</td>
    <td>260 °C</td>
    <td>260 °C</td>
    <td>260 °C</td>
  </tr>
  <tr>
    <td>1.6 mm - 2.5 mm</td>
    <td>260 °C</td>
    <td>250 °C</td>
    <td>245 °C</td>
  </tr>
  <tr>
    <td>≥ 2.5 mm</td>
    <td>250 °C</td>
    <td>245 °C</td>
    <td>245 °C</td>
  </tr>
</table>

## Reliability Test Program

<table>
  <tr>
    <th align="left">Test item</th>
    <th align="left">Method</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td>SOLDERABILITY</td>
    <td>JESD-22, B102</td>
    <td>5 Sec, 245 °C</td>
  </tr>
  <tr>
    <td>HTRB</td>
    <td>JESD-22, A108</td>
    <td>1000 Hrs, 80% of V<sub>DS</sub> max @ T<sub>jmax</sub></td>
  </tr>
  <tr>
    <td>HTGB</td>
    <td>JESD-22, A108</td>
    <td>1000 Hrs, 100% of V<sub>GS</sub> max @ T<sub>jmax</sub></td>
  </tr>
  <tr>
    <td>PCT</td>
    <td>JESD-22, A102</td>
    <td>168 Hrs, 100%RH, 2atm, 121 °C</td>
  </tr>
  <tr>
    <td>TCT</td>
    <td>JESD-22, A104</td>
    <td>500 Cycles, -65 °C~150 °C</td>
  </tr>
</table>

## Customer Service

**深圳市南芯微电子有限公司**

地址：深圳市光明区华强创意产业园4A座501 

电话: 0755 - 8254 3799

手机: 139 0294 5318（朱小姐）

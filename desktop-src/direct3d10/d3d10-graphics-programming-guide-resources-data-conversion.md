---
description: The following sections describe how Direct3D handles conversions between data types.
ms.assetid: 454d3fd0-fc0f-46a9-925e-13f8e3c39f02
title: Data Conversion Rules
ms.topic: article
ms.date: 05/31/2018
---

# Data Conversion Rules

The following sections describe how Direct3D handles conversions between data types.

-   [Data Type Terminology](#data-type-terminology)
-   [Floating Point Conversion](#floating-point-conversion)
    -   [Conververting from a higher range representation to a lower range representation](#conververting-from-a-higher-range-representation-to-a-lower-range-representation)
    -   [Converting from a lower range representation to a higher range representation](#converting-from-a-lower-range-representation-to-a-higher-range-representation)
-   [Integer Conversion](#integer-conversion)
-   [Fixed Point Integer Conversion](#fixed-point-integer-conversion)
-   [Related topics](#related-topics)

## Data Type Terminology

The following set of terms are subsequently used to characterize various format conversions.



| Term  | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNORM | Signed normalized integer, meaning that for an n-bit 2's complement number, the maximum value means 1.0f (e.g. the 5-bit value 01111 maps to 1.0f), and the minimum value means -1.0f (e.g. the 5-bit value 10000 maps to -1.0f). In addition, the second-minimum number maps to -1.0f (e.g. the 5-bit value 10001 maps to -1.0f). There are thus two integer representations for -1.0f. There is a single representation for 0.0f, and a single representation for 1.0f. This results in a set of integer representations for evenly spaced floating point values in the range (-1.0f...0.0f), and also a complementary set of representations for numbers in the range (0.0f...1.0f) |
| UNORM | Unsigned normalized integer, meaning that for an n-bit number, all 0's means 0.0f, and all 1's means 1.0f. A sequence of evenly spaced floating point values from 0.0f to 1.0f are represented. e.g. a 2-bit UNORM represents 0.0f, 1/3, 2/3, and 1.0f.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SINT  | Signed integer. 2's complement integer. e.g. an 3-bit SINT represents the integral values -4, -3, -2, -1, 0, 1, 2, 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| UINT  | Unsigned integer. e.g. a 3-bit UINT represents the integral values 0, 1, 2, 3, 4, 5, 6, 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| FLOAT | A floating-point value in any of the representations defined by Direct3D.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SRGB  | Similar to UNORM, in that for an n-bit number, all 0's means 0.0f and all 1's means 1.0f. However unlike UNORM, with SRGB the sequence of unsigned integer encodings between all 0's to all 1's represent a nonlinear progression in the floating point interpretation of the numbers, between 0.0f to 1.0f. Roughly, if this nonlinear progression, SRGB, is displayed as a sequence of colors, it would appear as a linear ramp of luminosity levels to an "average" observer, under "average" viewing conditions, on an "average" display. For complete detail, refer to the SRGB color standard, IEC 61996-2-1, at IEC (International Electrotechnical Commission).                |



 

## Floating Point Conversion

Whenever a floating point conversion between different representations occurs, including to or from non-floating point representations, the following rules apply.

### Conververting from a higher range representation to a lower range representation

-   Round-to-zero is used during conversion to another float format. If the target is an integer or fixed point format, round-to-nearest-even is used, unless the conversion is explicitly documented as using another rounding behavior, such as round-to-nearest for FLOAT to SNORM, FLOAT to UNORM or FLOAT to SRGB. Other exceptions are the ftoi and ftou shader instructions, which use round-to-zero. Finally, the float-to-fixed conversions used by the texture sampler and rasterizer have a specified tolerance measured in Unit-Last-Place from an infinitely precise ideal.
-   For source values greater than the dynamic range of a lower range target format (eg. a large 32-bit float value is written into a 16-bit float RenderTarget), the maximum representable (appropriately signed) value results, NOT including signed infinity (due to the round to zero described above).
-   NaN in a higher range format will be converted to NaN representation in the lower range format if the NaN representation exists in the lower range format. If the lower format does not have a NaN representation, the result will be 0.
-   INF in a higher range format will be converted to INF in the lower range format if available. If the lower format does not have an INF representation, it will be converted to the maximum value representable. The sign will be preserved if available in the target format.
-   Denorm in a higher range format will be converted to the Denorm representation in the lower range format if available in the lower range format and the conversion is possible, otherwise the result is 0. The sign bit will be preserved if available in the target format.

### Converting from a lower range representation to a higher range representation

-   NaN in a lower range format will be converted to the NaN representation in the higher range format if available in the higher range format. If the higher range format does not have a NaN representation, it will be converted to 0.
-   INF in a lower range format will be converted to the INF representation in the higher range format if available in the higher range format. If the higher format does not have an INF representation, it will be converted to the maximum value representable (MAX\_FLOAT in that format). The sign will be preserved if available in the target format.
-   Denorm in a lower range format will be converted to a normalized representation in the higher range format if possible, or else to a Denorm representation in the higher range format if the Denorm representation exists. Failing those, if the higher range format does not have a Denorm representation, it will be converted to 0. The sign will be preserved if available in the target format. Note that 32-bit float numbers count as a format without a Denorm representation (because Denorms in operations on 32-bit floats flush to sign preserved 0).

## Integer Conversion

The following table describes conversions from various representations described above to other representations. Only conversions that actually occur in Direct3D are shown.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Source Data Type</th>
<th>Destination Data Type</th>
<th>Conversion Rule</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SNORM</td>
<td>FLOAT</td>
<td>Given an n-bit integer value representing the signed range [-1.0f to 1.0f], conversion to floating-point is as follows.<br/>
<ul>
<li>The most-negative value maps to -1.0f. e.g. the 5-bit value 10000 maps to -1.0f.</li>
<li>Every other value is converted to a float (call it c), and then result = c * (1.0f / (2⁽ⁿ⁻¹⁾-1)). For example the 5-bit value 10001 is converted to -15.0f, and then divided by 15.0f, yielding -1.0f.</li>
</ul></td>
</tr>
<tr class="even">
<td>FLOAT</td>
<td>SNORM</td>
<td>Given a floating-point number, conversion to an n-bit integer value representing the signed range [-1.0f to 1.0f] is as follows.<br/>
<ul>
<li>Let c represent the starting value.</li>
<li>If c is NaN, the result is 0.</li>
<li>If c > 1.0f, including INF, it is clamped to 1.0f.</li>
<li>If c < -1.0f, including -INF, it is clamped to -1.0f.</li>
<li>Convert from float scale to integer scale: c = c * (2ⁿ⁻¹-1).</li>
<li>Convert to an integer as follows.
<ul>
<li>If c >= 0 then c = c + 0.5f, otherwise, c = c - 0.5f.</li>
<li>Drop the decimal fraction, and the remaining floating point (integral) value is converted directly to an integer.</li>
</ul></li>
</ul>
This conversion is permitted a tolerance of D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_Unit-Last-Place Unit-Last-Place (on the integer side). This means that after converting from float to integer scale, any value within D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place of a representable target format value is permitted to map to that value. The additional Data Invertability requirement ensures that the conversion is nondecreasing across the range and all output values are attainable. (In the constants shown here, <em>xx</em> should be replaced with the Direct3D version, for example 10, 11, or 12.)<br/></td>
</tr>
<tr class="odd">
<td>UNORM</td>
<td>FLOAT</td>
<td>The starting n-bit value is converted to float (0.0f, 1.0f, 2.0f, etc.) and then divided by (2ⁿ-1).<br/></td>
</tr>
<tr class="even">
<td>FLOAT</td>
<td>UNORM</td>
<td>Let c represent the starting value.<br/>
<ul>
<li>If c is NaN, the result is 0.</li>
<li>If c > 1.0f, including INF, it is clamped to 1.0f.</li>
<li>If c < 0.0f, including -INF, it is clamped to 0.0f.</li>
<li>Convert from float scale to integer scale: c = c * (2ⁿ-1).</li>
<li>Convert to integer.
<ul>
<li>c = c + 0.5f.</li>
<li>The decimal fraction is dropped, and the remaining floating point (integral) value is converted directly to an integer.</li>
</ul></li>
</ul>
This conversion is permitted a tolerance of D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place (on the integer side). This means that after converting from float to integer scale, any value within D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place of a representable target format value is permitted to map to that value. The additional Data Invertability requirement ensures that the conversion is nondecreasing across the range and all output values are attainable.<br/></td>
</tr>
<tr class="odd">
<td>SRGB</td>
<td>FLOAT</td>
<td>The following is the ideal SRGB to FLOAT conversion.<br/>
<ul>
<li>Take the starting n-bit value, convert it a float (0.0f, 1.0f, 2.0f, etc.); call this c.</li>
<li>c = c * (1.0f / (2ⁿ-1))</li>
<li>If (c < = D3D<em>xx</em>_SRGB_TO_FLOAT_THRESHOLD) then: result = c / D3D<em>xx</em>_SRGB_TO_FLOAT_DENOMINATOR_1, else: result = ((c + D3D<em>xx</em>_SRGB_TO_FLOAT_OFFSET)/D3D<em>xx</em>_SRGB_TO_FLOAT_DENOMINATOR_2)D3D<em>xx</em>_SRGB_TO_FLOAT_EXPONENT</li>
</ul>
This conversion is permitted a tolerance of D3D<em>xx</em>_SRGB_TO_FLOAT_TOLERANCE_IN_ULP Unit-Last-Place (on the SRGB side). <br/></td>
</tr>
<tr class="even">
<td>FLOAT</td>
<td>SRGB</td>
<td>The following is the ideal FLOAT -> SRGB conversion.<br/> Assuming the target SRGB color component has n bits:<br/>
<ul>
<li>Suppose the starting value is c.</li>
<li>If c is NaN, the result is 0.</li>
<li>If c > 1.0f, including INF, is clamped to 1.0f.</li>
<li>If c < 0.0f, including -INF, it is clamped to 0.0f.</li>
<li>If (c <= D3D<em>xx</em>_FLOAT_TO_SRGB_THRESHOLD) then: c = D3D<em>xx</em>_FLOAT_TO_SRGB_SCALE_1 * c, else: c = D3D<em>xx</em>_FLOAT_TO_SRGB_SCALE_2 * c(D3D<em>xx</em>_FLOAT_TO_SRGB_EXPONENT_NUMERATOR/D3D<em>xx</em>_FLOAT_TO_SRGB_EXPONENT_DENOMINATOR) - D3D<em>xx</em>_FLOAT_TO_SRGB_OFFSET</li>
<li>Convert from float scale to integer scale: c = c * (2ⁿ-1).</li>
<li>Convert to integer:
<ul>
<li>c = c + 0.5f.</li>
<li>The decimal fraction is dropped, and the remaining floating point (integral) value is converted directly to an integer.</li>
</ul></li>
</ul>
This conversion is permitted a tolerance of D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place (on the integer side). This means that after converting from float to integer scale, any value within D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place of a representable target format value is permitted to map to that value. The additional Data Invertability requirement ensures that the conversion is nondecreasing across the range and all output values are attainable.<br/></td>
</tr>
<tr class="odd">
<td>SINT</td>
<td>SINT With More Bits</td>
<td>To convert from SINT to an SINT with more bits, the most significant bit (MSB) of the starting number is &quot;sign-extended&quot; to the additional bits available in the target format.<br/></td>
</tr>
<tr class="even">
<td>UINT</td>
<td>SINT With More Bits</td>
<td>To convert from UINT to an SINT with more bits, the number is copied to the target format's least significant bits (LSBs) and additional MSBs are padded with 0.<br/></td>
</tr>
<tr class="odd">
<td>SINT</td>
<td>UINT With More Bits</td>
<td>To convert from SINT to UINT with more bits: If negative, the value is clamped to 0. Otherwise the number is copied to the target format's LSBs and additional MSB's are padded with 0.<br/></td>
</tr>
<tr class="even">
<td>UINT</td>
<td>UINT With More Bits</td>
<td>To convert from UINT to UINT with more bits the number is copied to the target format's LSBs and additional MSB's are padded with 0.<br/></td>
</tr>
<tr class="odd">
<td>SINT or UINT</td>
<td>SINT or UINT With Fewer or Equal Bits</td>
<td>To convert from a SINT or UINT to SINT or UINT with fewer or equal bits (and/or change in signedness), the starting value is simply clamped to the range of the target format.<br/></td>
</tr>
</tbody>
</table>



 

## Fixed Point Integer Conversion

Fixed point integers are simply integers of some bit size that have an implicit decimal point at a fixed location.

The ubiquitous "integer" data type is a special case of a fixed point integer with the decimal at the end of the number.

Fixed point number representations are characterized as: i.f, where i is the number of integer bits and f is the number of fractional bits. e.g. 16.8 means 16 bits integer followed by 8 bits of fraction. The integer part is stored in 2's complement, at least as defined here (though it can be defined equally for unsigned integers as well). The fractional part is stored in unsigned form. The fractional part always represents the positive fraction between the two nearest integral values, starting from the most negative.

Addition and subtraction operations on fixed point numbers are performed simply using standard integer arithmetic, without any consideration for where the implied decimal lies. Adding 1 to a 16.8 fixed point number just means adding 256, since the decimal is 8 places in from the least significant end of the number. Other operations such as multiplication, can be performed as well simply using integer arithmetic, provided the effect on the fixed decimal is accounted for. For example, multiplying two 16.8 integers using an integer multiply produces a 32.16 result.

Fixed point integer representations are used in two ways in Direct3D.

-   Post-clipped vertex positions in the rasterizer are snapped to fixed point, to uniformly distribute precision across the RenderTarget area. Many rasterizer operations, including face culling as one example, occur on fixed point snapped positions, while other operations, such as attribute interpolator setup, use positions that have been converted back to floating point from the fixed point snapped positions.
-   Texture coordinates for sampling operations are snapped to fixed point (after being scaled by texture size), to uniformly distribute precision across texture space, in choosing filter tap locations/weights. Weight values are converted back to floating point before actual filtering arithmetic is performed.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Source Data Type</th>
<th>Destination Data Type</th>
<th>Conversion Rule</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FLOAT</td>
<td>Fixed Point Integer</td>
<td>The following is the general procedure for converting a floating point number n to a fixed point integer i.f, where i is the number of (signed) integer bits and f is the number of fractional bits.<br/>
<ul>
<li>Compute FixedMin = -2⁽ⁱ⁻¹⁾</li>
<li>Compute FixedMax = 2⁽ⁱ⁻¹⁾ - 2<sup>(-f)</sup></li>
<li>If n is a NaN, result = 0; if n is +Inf, result = FixedMax*2<sup>f</sup>; if n is -Inf, result = FixedMin*2<sup>f</sup></li>
<li>If n >= FixedMax, result = Fixedmax*2<sup>f</sup>; if n <= FixedMin, result = FixedMin*2<sup>f</sup></li>
<li>Else compute n*2<sup>f</sup> and convert to integer.</li>
</ul>
Implementations are permitted D3D<em>xx</em>_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP Unit-Last-Place tolerance in the integer result, instead of the infinitely precise value n*2<sup>f</sup> after the last step above.<br/></td>
</tr>
<tr class="even">
<td>Fixed Point Integer</td>
<td>FLOAT</td>
<td>Assume that the specific fixed point representation being converted to float does not contain more than a total of 24 bits of information, no more than 23 bits of which is in the fractional component. Suppose a given fixed point number, fxp, is in i.f form (i bits integer, f bits fraction). The conversion to float is akin to the following pseudocode.<br/> float result = (float)(fxp >> f) + // extract integer<br/> <dl> ((float)(fxp & (2<sup>f</sup> - 1)) / (2<sup>f</sup>)); // extract fraction<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 





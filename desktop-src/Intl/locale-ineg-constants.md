---
description: This topic defines the LOCALE\_INEG\* constants used by NLS.
ms.assetid: 3a1e4a63-31bd-4ff9-a3ca-af357389e179
title: LOCALE_INEG* Constants
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_INEG\* Constants

This topic defines the LOCALE\_INEG\* constants used by NLS.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LOCALE_INEGCURR</td>
<td>Negative currency mode. 
<table>
<thead>
<tr class="header">
<th>Mode</th>
<th>Format for negative currency</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Left parenthesis, monetary symbol, number, right parenthesis; for example, ($1.1)</td>
</tr>
<tr class="even">
<td>1</td>
<td>Negative sign, monetary symbol, number; for example, -$1.1</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Monetary symbol, negative sign, number; for example, $-1.1</td>
</tr>
<tr class="even">
<td>3</td>
<td>Monetary symbol, number, negative sign; for example, $1.1-</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Left parenthesis, number, monetary symbol, right parenthesis; for example, (1.1$)</td>
</tr>
<tr class="even">
<td>5</td>
<td>Negative sign, number, monetary symbol; for example, -1.1$</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Number, negative sign, monetary symbol; for example, 1.1-$</td>
</tr>
<tr class="even">
<td>7</td>
<td>Number, monetary symbol, negative sign; for example, 1.1$-</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Negative sign, number, space, monetary symbol (like #5, but with a space before the monetary symbol); for example, -1.1 $</td>
</tr>
<tr class="even">
<td>9</td>
<td>Negative sign, monetary symbol, space, number (like #1, but with a space after the monetary symbol); for example, -$ 1.1</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Number, space, monetary symbol, negative sign (like #7, but with a space before the monetary symbol); for example, 1.1 $-</td>
</tr>
<tr class="even">
<td>11</td>
<td>Monetary symbol, space, number, negative sign (like #3, but with a space after the monetary symbol); for example, $ 1.1-</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Monetary symbol, space, negative sign, number (like #2, but with a space after the monetary symbol); for example, $ -1.1</td>
</tr>
<tr class="even">
<td>13</td>
<td>Number, negative sign, space, monetary symbol (like #6, but with a space before the monetary symbol); for example, 1.1- $</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Left parenthesis, monetary symbol, space, number, right parenthesis (like #0, but with a space after the monetary symbol); for example, ($ 1.1)</td>
</tr>
<tr class="even">
<td>15</td>
<td>Left parenthesis, number, space, monetary symbol, right parenthesis (like #4, but with a space before the monetary symbol); for example, (1.1 $)</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>LOCALE_INEGNUMBER</td>
<td>Negative number mode, that is, the format for a negative number. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Left parenthesis, number, right parenthesis; for example, (1.1)</td>
</tr>
<tr class="even">
<td>1</td>
<td>Negative sign, number; for example, -1.1</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Negative sign, space, number; for example, - 1.1</td>
</tr>
<tr class="even">
<td>3</td>
<td>Number, negative sign; for example, 1.1-</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Number, space, negative sign; for example, 1.1 -</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>LOCALE_INEGSEPBYSPACE</td>
<td>Separation of the negative sign in a monetary value. This value is 1 if the monetary symbol is separated by a space from the negative amount, or 0 if it is not.</td>
</tr>
<tr class="even">
<td>LOCALE_INEGSIGNPOSN</td>
<td>Formatting index for the negative sign in currency values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Parentheses surround the amount and the monetary symbol.</td>
</tr>
<tr class="even">
<td>1</td>
<td>The sign precedes the number.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>The sign follows the number.</td>
</tr>
<tr class="even">
<td>3</td>
<td>The sign precedes the monetary symbol.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>The sign follows the monetary symbol.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>LOCALE_INEGSYMPRECEDES</td>
<td>Position of the monetary symbol in a negative monetary value. This value is 1 if the monetary symbol precedes the negative amount, or 0 if the symbol follows the amount.</td>
</tr>
</tbody>
</table>



 

 

 




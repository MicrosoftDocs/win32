---
description: Multiplication operators.
ms.assetid: f8397999-9956-4d11-8705-c95b788a9f03
title: operator * operators
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- NA
api_location: 
---

# operator \* operators

Multiplication operators

### Overload list



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Operator</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><a href="/previous-versions/windows/desktop/legacy/ee421390(v=vs.85)"><strong>XMVECTOR::operator * (float,XMVECTOR)</strong></a></td>
<td style="text-align: left;">Multiply a floating point value by an instance of <code>XMVECTOR</code>, returning the result a new instance of <code>XMVECTOR</code>.<br/> The <code>operator *</code> multiplies a floating point value against each component of an instance of <a href="xmvector-data-type.md"><strong>XMVECTOR Data Type</strong></a>, returning a new <code>XMVECTOR</code> instance whose components contain the result. <br/>
<blockquote>
[!Note]<br />
This operator is only available under C++.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="/previous-versions/windows/desktop/legacy/ee421391(v=vs.85)"><strong>XMVECTOR::operator * (XMVECTOR,float)</strong></a></td>
<td style="text-align: left;">Multiply an instance of <code>XMVECTOR</code> by a floating point value, returning the result a new instance of <code>XMVECTOR</code>.<br/> The <code>operator *</code> multiplies each component of an instance of <a href="xmvector-data-type.md"><strong>XMVECTOR Data Type</strong></a> by a floating point value, returning a new <code>XMVECTOR</code> instance whose components contain the result. <br/>
<blockquote>
[!Note]<br />
This operator is only available under C++.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="/previous-versions/windows/desktop/legacy/ee421392(v=vs.85)"><strong>XMVECTOR::operator * (XMVECTOR,XMVECTOR)</strong></a></td>
<td style="text-align: left;">Multiplies one instance of <code>XMVECTOR</code> by a second instance, returning the result in a third instance. <br/> The <code>operator *</code> multiplies each component of an instance of <a href="xmvector-data-type.md"><strong>XMVECTOR Data Type</strong></a> by the corresponding component in a second instance of <code>XMVECTOR</code>, returning a new <code>XMVECTOR</code> instance containing the result. <br/>
<blockquote>
[!Note]<br />
This operator is only available under C++.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



## See also

<dl> <dt>

[XMVECTOR Operators](ovw-xmvector-operators.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**XMVECTOR Data Type**](xmvector-data-type.md)
</dt> </dl>

 

 

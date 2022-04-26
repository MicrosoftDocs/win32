---
description: The following constants are provided by the DirectXMath Library.
ms.assetid: a206fe22-12c8-ac2b-ee37-20cfff35841a
title: DirectXMath Library constants
ms.topic: reference
ms.date: 05/31/2018
---

# DirectXMath Library constants

The following constants are provided by the DirectXMath Library.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIRECTXMATH_VERSION<br/></td>
<td>The version of the DirectXMath Library. The initial preview release was 300, the Windows 8 final version is 303, the Windows 8.1 version is 305. XNA Math's versions were 200, 201, 202, 203, 204, and so on. This is defined as a preprocessor symbol.<br/></td>
</tr>
<tr class="even">
<td>XM_PI<br/></td>
<td>An optimal representation of π.<br/></td>
</tr>
<tr class="odd">
<td>XM_2PI<br/></td>
<td>An optimal representation of 2*π.<br/></td>
</tr>
<tr class="even">
<td>XM_1DIVPI<br/></td>
<td>An optimal representation of 1/π.<br/></td>
</tr>
<tr class="odd">
<td>XM_1DIV2PI<br/></td>
<td>An optimal representation of 1/2π.<br/></td>
</tr>
<tr class="even">
<td>XM_PIDIV2<br/></td>
<td>An optimal representation of π/2.<br/></td>
</tr>
<tr class="odd">
<td>XM_PIDIV4<br/></td>
<td>An optimal representation of π/4.<br/></td>
</tr>
<tr class="even">
<td>XM_PERMUTE_0X<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the X component of the first of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="odd">
<td>XM_PERMUTE_0Y<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the Y component of the first of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_PERMUTE_0Z<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the Z component of the first of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="odd">
<td>XM_PERMUTE_0W<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the W component of the first of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_PERMUTE_1X<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the X component of the second of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="odd">
<td>XM_PERMUTE_1Y<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the Y component of the second of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_PERMUTE_1Z<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the Z component of the second of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="odd">
<td>XM_PERMUTE_1W<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorpermute"><strong>XMVectorPermute</strong></a>. This indicates that the W component of the second of the vector arguments to <strong>XMVectorPermute</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_SELECT_0<br/></td>
<td>A constant used to construct a control vector used with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorselect"><strong>XMVectorSelect</strong></a>. Indicates that the component of the first of the vector arguments to <strong>XMVectorSelect</strong> is to be copied to the index location in a result vector corresponding to its index in the control vector.<br/> For example, a control vector with XM_SELECT_0 as its second component copies the second component of the first vector to the second component of the result vector. <br/></td>
</tr>
<tr class="odd">
<td>XM_SELECT_1<br/></td>
<td>A constant used to construct a control vector used with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorselect"><strong>XMVectorSelect</strong></a>. Indicates that the component of the second of the vector arguments to <strong>XMVectorSelect</strong> is to be copied to the index location in a result vector corresponding to its index in the control vector. <br/> For example, a control vector with XM_SELECT_1 as its second component copies the second component of the second vector to the second component of the result vector. <br/></td>
</tr>
<tr class="even">
<td>XM_SWIZZLE_X<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorswizzle"><strong>XMVectorSwizzle</strong></a>. This indicates that the X component of the vector argument to <strong>XMVectorSwizzle</strong> is to be copied to the index location in a result vector corresponding to the specified element.<br/></td>
</tr>
<tr class="odd">
<td>XM_SWIZZLE_Y<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorswizzle"><strong>XMVectorSwizzle</strong></a>. This indicates that the Y component of the vector argument to <strong>XMVectorSwizzle</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_SWIZZLE_Z<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorswizzle"><strong>XMVectorSwizzle</strong></a>. This indicates that the Z component of the vector argument to <strong>XMVectorSwizzle</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="odd">
<td>XM_SWIZZLE_W<br/></td>
<td>A constant used as an element index with <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvectorswizzle"><strong>XMVectorSwizzle</strong></a>. This indicates that the W component of the vector argument to <strong>XMVectorSwizzle</strong> is to be copied to the index location in a result vector corresponding to the specified element. <br/></td>
</tr>
<tr class="even">
<td>XM_CRMASK_CR6<br/></td>
<td>Mask to get a comparison result, which is typically retrieved using a recording version of an DirectXMath function such <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvector4equalr"><strong>XMVector4EqualR</strong></a>. The following example gets the comparison result from the variable CR:
<pre class="syntax" data-space="preserve"><code>uint32_t val = ((CR) & XM_CRMASK_CR6);</code></pre>
<br/></td>
</tr>
<tr class="odd">
<td>XM_CRMASK_CR6TRUE<br/></td>
<td>Mask to get a comparison result, and verify if it is a logical true. The value is typically retrieved using a recording version of a DirectXMath function such as <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvector4equalr"><strong>XMVector4EqualR</strong></a>. The example checks if the variableq CR is true:
<pre class="syntax" data-space="preserve"><code>bool val = (((CR) & XM_CRMASK_CR6FALSE) == XM_CRMASK_CR6FALSE);</code></pre>
See also <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonanytrue"><strong>XMComparisonAnyTrue</strong></a>, <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonalltrue"><strong>XMComparisonAllTrue</strong></a>, and <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonmixed"><strong>XMComparisonMixed</strong></a><br/></td>
</tr>
<tr class="even">
<td>XM_CRMASK_CR6FALSE<br/></td>
<td>Mask to get a comparison result, and verify if it is a logical false. The value is typically retrieved using a recording version of an DirectXMath math function such as <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvector4equalr"><strong>XMVector4EqualR</strong></a>. The example checks if the variable CR is false:
<pre class="syntax" data-space="preserve"><code>bool val = (((CR) & XM_CRMASK_CR6FALSE) == XM_CRMASK_CR6FALSE);</code></pre>
See also <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonanyfalse"><strong>XMComparisonAnyFalse</strong></a>, <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonallfalse"><strong>XMComparisonAllFalse</strong></a> and <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonmixed"><strong>XMComparisonMixed</strong></a><br/></td>
</tr>
<tr class="odd">
<td>XM_CRMASK_CR6BOUNDS<br/></td>
<td>Mask to get a comparison result, and verify if the result indicates that some of the inputs were out of bounds. The value is typically retrieved using a recording version of a DirectXMath function such as <a href="/windows/desktop/api/directxmath/nf-directxmath-xmvector4equalr"><strong>XMVector4EqualR</strong></a>. The example checks if the variable CR indicates and out of bounds state.
<pre class="syntax" data-space="preserve"><code>bool val = (((CR) & XM_CRMASK_CR6BOUNDS) == XM_CRMASK_CR6BOUNDS);</code></pre>
See also <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonallinbounds"><strong>XMComparisonAllInBounds</strong></a> and <a href="/windows/desktop/api/DirectXMath/nf-directxmath-xmcomparisonanyoutofbounds"><strong>XMComparisonAnyOutOfBounds</strong></a><br/></td>
</tr>
<tr class="even">
<td>Colors::AliceBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::AntiqueWhite</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Aqua</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Aquamarine</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Azure</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Beige</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Bisque</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Black</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::BlanchedAlmond</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Blue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::BlueViolet</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Brown</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::BurlyWood</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::CadetBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Chartreuse</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Chocolate</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Coral</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::CornflowerBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Cornsilk</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Crimson</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Cyan</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkCyan</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkGoldenrod</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkKhaki</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkMagenta</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkOliveGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkOrange</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkOrchid</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkRed</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkSalmon</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkSeaGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkSlateBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkSlateGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DarkTurquoise</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DarkViolet</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DeepPink</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DeepSkyBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::DimGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::DodgerBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Firebrick</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::FloralWhite</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::ForestGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Fuchsia</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Gainsboro</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::GhostWhite</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Gold</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Goldenrod</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Gray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Green</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::GreenYellow</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Honeydew</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::HotPink</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::IndianRed</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Indigo</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Ivory</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Khaki</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Lavender</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LavenderBlush</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LawnGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LemonChiffon</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightCoral</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightCyan</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightGoldenrodYellow</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightPink</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightSalmon</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightSeaGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightSkyBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightSlateGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::LightSteelBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LightYellow</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Lime</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::LimeGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Linen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Magenta</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Maroon</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MediumAquamarine</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MediumBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MediumOrchid</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MediumPurple</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MediumSeaGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MediumSlateBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MediumSpringGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MediumTurquoise</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MediumVioletRed</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MidnightBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::MintCream</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::MistyRose</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Moccasin</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::NavajoWhite</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Navy</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::OldLace</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Olive</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::OliveDrab</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Orange</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::OrangeRed</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Orchid</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::PaleGoldenrod</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::PaleGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::PaleTurquoise</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::PaleVioletRed</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::PapayaWhip</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::PeachPuff</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Peru</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Pink</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Plum</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::PowderBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Purple</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Red</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::RosyBrown</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::RoyalBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::SaddleBrown</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Salmon</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::SandyBrown</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::SeaGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::SeaShell</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Sienna</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Silver</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::SkyBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::SlateBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::SlateGray</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Snow</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::SpringGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::SteelBlue</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Tan</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Teal</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Thistle</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Tomato</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Transparent</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Turquoise</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Violet</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::Wheat</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::White</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::WhiteSmoke</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="odd">
<td>Colors::Yellow</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
<tr class="even">
<td>Colors::YellowGreen</td>
<td>Constants for the standard .NET color definitions. These values are R, G, B data that can be used as XMVECTOR's or passed directly to the Direct3D 10.x / Direct3D 11 API's Clear method.</td>
</tr>
</tbody>
</table>



 

> [!Note]
>
> All the Colors constants are defined in the standard [sRGB](https://en.wikipedia.org/wiki/SRGB) color space (as are .NET colors and HTML web-safe colors). For gamma-correct rendering using linear color space, the values need to be adjusted slightly.

 

## Related Topics

<dl> <dt>

<span id="DirectXMath_Programming_Reference"></span><span id="directxmath_programming_reference"></span><span id="DIRECTXMATH_PROGRAMMING_REFERENCE"></span>[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> <dd></dd> </dl>

## Related topics

<dl> <dt>

[DirectXMath Programming Reference](ovw-xnamath-reference.md)
</dt> </dl>

 

 

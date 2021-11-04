---
title: D3DX12SerializeVersionedRootSignature function (D3dx12.h)
description: Helps enable root signature 1.1 features when they are available, and does not require maintaining two code paths for building root signatures. This helper method reconstructs a version 1.0 root signature when version 1.1 is not supported.
ms.assetid: 0F6BA6C1-9A33-4E99-BF34-4A0358E7427D
keywords:
- D3DX12SerializeVersionedRootSignature function
topic_type:
- apiref
api_name:
- D3DX12SerializeVersionedRootSignature
api_location:
- D3D12.dll
api_type:
- DllExport
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX12SerializeVersionedRootSignature function

Helps enable root signature 1.1 features when they are available, and does not require maintaining two code paths for building root signatures. This helper method reconstructs a version 1.0 root signature when version 1.1 is not supported.

## Syntax


```C++
HRESULT inline D3DX12SerializeVersionedRootSignature(
  _In_      const D3D12_VERSIONED_ROOT_SIGNATURE_DESC *pRootSignatureDesc,
                  D3D_ROOT_SIGNATURE_VERSION          MaxVersion,
  _Out_           ID3DBlob                            **ppBlob,
  _Out_opt_       ID3DBlob                            **ppErrorBlob
);
```



## Parameters

<dl> <dt>

*pRootSignatureDesc* \[in\]
</dt> <dd>

Type: **const D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC\***

Specifies a [**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) that contains a description of any version of a root signature.

</dd> <dt>

*MaxVersion* 
</dt> <dd>

Type: **D3D\_ROOT\_SIGNATURE\_VERSION**

Specifies the maximum supported [**D3D\_ROOT\_SIGNATURE\_VERSION**](/windows/desktop/api/d3d12/ne-d3d12-d3d_root_signature_version).

</dd> <dt>

*ppBlob* \[out\]
</dt> <dd>

Type: **ID3DBlob\*\***

A pointer to a memory block that receives a pointer to the [**ID3DBlob**](/previous-versions/windows/desktop/legacy/ff728743(v=vs.85)) interface that you can use to access the serialized root signature.

</dd> <dt>

*ppErrorBlob* \[out, optional\]
</dt> <dd>

Type: **ID3DBlob\*\***

A pointer to a memory block that receives a pointer to the [**ID3DBlob**](/previous-versions/windows/desktop/legacy/ff728743(v=vs.85)) interface that you can use to access serializer error messages, or **NULL** if there are no errors.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns **S\_OK** if successful; otherwise, returns one of the [Direct3D 12 Return Codes](d3d12-graphics-reference-returnvalues.md).

## Remarks

This function was released to coincide with the Windows 10 Anniversary Update (14393). In order to support Windows 10 versions prior to this, use of this function requires d3d12.lib be set up for *delay loading*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[**D3D12SerializeVersionedRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-d3d12serializeversionedrootsignature)
</dt> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> </dl>

 


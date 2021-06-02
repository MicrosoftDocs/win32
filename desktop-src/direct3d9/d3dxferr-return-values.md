---
description: The methods used to work with DirectX .x files can return the following values in addition to the standard COM return values.
ms.assetid: b1d04fab-25cb-431d-942e-74092bc9c5c2
title: D3DXFERR Return Values (D3dx9xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFERR
api_type: 
- HeaderDef
api_location: 
- d3dx9xof.h
---

# D3DXFERR Return Values

The methods used to work with DirectX .x files can return the following values in addition to the standard COM return values.

<dl> <dt>

<span id="D3DXFERR_BADARRAYSIZE"></span><span id="d3dxferr_badarraysize"></span>**D3DXFERR\_BADARRAYSIZE**
</dt> <dd>

An array exceeds the allowable size.

</dd> <dt>

<span id="D3DXFERR_BADCACHEFILE"></span><span id="d3dxferr_badcachefile"></span>**D3DXFERR\_BADCACHEFILE**
</dt> <dd>

A cache file could not be read.

</dd> <dt>

<span id="D3DXFERR_BADDataReference"></span><span id="d3dxferr_baddatareference"></span><span id="D3DXFERR_BADDATAREFERENCE"></span>**D3DXFERR\_BADDataReference**
</dt> <dd>

Template member data could not be retrieved.

</dd> <dt>

<span id="D3DXFERR_BADFILE"></span><span id="d3dxferr_badfile"></span>**D3DXFERR\_BADFILE**
</dt> <dd>

A file read or write operation failed.

</dd> <dt>

<span id="D3DXFERR_BADFILEFLOATSIZE"></span><span id="d3dxferr_badfilefloatsize"></span>**D3DXFERR\_BADFILEFLOATSIZE**
</dt> <dd>

File is not the expected size.

</dd> <dt>

<span id="D3DXFERR_BADFILETYPE"></span><span id="d3dxferr_badfiletype"></span>**D3DXFERR\_BADFILETYPE**
</dt> <dd>

File has an invalid format.

</dd> <dt>

<span id="D3DXFERR_BADFILEVERSION"></span><span id="d3dxferr_badfileversion"></span>**D3DXFERR\_BADFILEVERSION**
</dt> <dd>

File has an invalid format version.

</dd> <dt>

<span id="D3DXFERR_BADOBJECT"></span><span id="d3dxferr_badobject"></span>**D3DXFERR\_BADOBJECT**
</dt> <dd>

Data could not be read from or written to an object.

</dd> <dt>

<span id="D3DXFERR_BADRESOURCE"></span><span id="d3dxferr_badresource"></span>**D3DXFERR\_BADRESOURCE**
</dt> <dd>

An operation on a resource failed.

</dd> <dt>

<span id="D3DXFERR_BADTYPE"></span><span id="d3dxferr_badtype"></span>**D3DXFERR\_BADTYPE**
</dt> <dd>

File did not match known template types.

</dd> <dt>

<span id="D3DXFERR_BADVALUE"></span><span id="d3dxferr_badvalue"></span>**D3DXFERR\_BADVALUE**
</dt> <dd>

A variable is outside its expected range; typically returned when an object pointer is invalid.

</dd> <dt>

<span id="D3DXFERR_FILENOTFOUND"></span><span id="d3dxferr_filenotfound"></span>**D3DXFERR\_FILENOTFOUND**
</dt> <dd>

A valid handle could not be found for the specified file.

</dd> <dt>

<span id="D3DXFERR_NOMOREDATA"></span><span id="d3dxferr_nomoredata"></span>**D3DXFERR\_NOMOREDATA**
</dt> <dd>

Pointer offset extended beyond the end of the buffer.

</dd> <dt>

<span id="D3DXFERR_NOMOREOBJECTS"></span><span id="d3dxferr_nomoreobjects"></span>**D3DXFERR\_NOMOREOBJECTS**
</dt> <dd>

No more child objects are available.

</dd> <dt>

<span id="D3DXFERR_NOTDONEYET"></span><span id="d3dxferr_notdoneyet"></span>**D3DXFERR\_NOTDONEYET**
</dt> <dd>

Data type did not match allowed types.

</dd> <dt>

<span id="D3DXFERR_NOTFOUND"></span><span id="d3dxferr_notfound"></span>**D3DXFERR\_NOTFOUND**
</dt> <dd>

Object could not be found from the specified parameters.

</dd> <dt>

<span id="D3DXFERR_PARSEERROR"></span><span id="d3dxferr_parseerror"></span>**D3DXFERR\_PARSEERROR**
</dt> <dd>

Data stream could not be parsed.

</dd> <dt>

<span id="D3DXFERR_RESOURCENOTFOUND"></span><span id="d3dxferr_resourcenotfound"></span>**D3DXFERR\_RESOURCENOTFOUND**
</dt> <dd>

A valid handle could not be found for the specified resource.

</dd> </dl>

## Remarks

The .x file error facility code \_FACD3DXF is used to generate error codes. For example:


```
#define _FACD3DXF           0x876
#define D3DXFERR_BADOBJECT  MAKE_HRESULT( 1, _FACD3DXF, 900 )
```



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9xof.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX X File Constants](dx9-graphics-reference-d3dx-x-file-constants.md)
</dt> </dl>

 

 





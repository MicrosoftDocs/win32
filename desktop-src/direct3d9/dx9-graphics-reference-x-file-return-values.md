---
description: The methods used to work with DirectX .x files can return the following values in addition to the standard COM return values. Deprecated.
ms.assetid: a91168bc-966a-47b5-ba83-fc480593228d
title: Return Values (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Return
api_type: 
- HeaderDef
api_location: 
- DXFile.h
---

# Return Values (DXFile.h)

The methods used to work with DirectX .x files can return the following values in addition to the standard COM return values. Deprecated.

<dl> <dt>

<span id="DXFILE_OK"></span><span id="dxfile_ok"></span>**DXFILE\_OK**
</dt> <dd>

Command completed successfully.

</dd> <dt>

<span id="DXFILEERR_BADALLOC"></span><span id="dxfileerr_badalloc"></span>**DXFILEERR\_BADALLOC**
</dt> <dd>

Memory allocation failed.

</dd> <dt>

<span id="DXFILEERR_BADARRAYSIZE"></span><span id="dxfileerr_badarraysize"></span>**DXFILEERR\_BADARRAYSIZE**
</dt> <dd>

Array size is invalid.

</dd> <dt>

<span id="DXFILEERR_BADCACHEFILE"></span><span id="dxfileerr_badcachefile"></span>**DXFILEERR\_BADCACHEFILE**
</dt> <dd>

The cache file containing the .x file date is invalid. A cache file contains data retrieved from the network, cached on the hard disk, and retrieved in subsequent requests.

</dd> <dt>

<span id="DXFILEERR_BADDataReference"></span><span id="dxfileerr_baddatareference"></span><span id="DXFILEERR_BADDATAREFERENCE"></span>**DXFILEERR\_BADDataReference**
</dt> <dd>

Data reference is invalid.

</dd> <dt>

<span id="DXFILEERR_BADFILE"></span><span id="dxfileerr_badfile"></span>**DXFILEERR\_BADFILE**
</dt> <dd>

File is invalid.

</dd> <dt>

<span id="DXFILEERR_BADFILECOMPRESSIONTYPE"></span><span id="dxfileerr_badfilecompressiontype"></span>**DXFILEERR\_BADFILECOMPRESSIONTYPE**
</dt> <dd>

File compression type is invalid.

</dd> <dt>

<span id="DXFILEERR_BADFILEFLOATSIZE"></span><span id="dxfileerr_badfilefloatsize"></span>**DXFILEERR\_BADFILEFLOATSIZE**
</dt> <dd>

Floating-point size is invalid.

</dd> <dt>

<span id="DXFILEERR_BADFILETYPE"></span><span id="dxfileerr_badfiletype"></span>**DXFILEERR\_BADFILETYPE**
</dt> <dd>

File is not a DirectX .x file.

</dd> <dt>

<span id="DXFILEERR_BADFILEVERSION"></span><span id="dxfileerr_badfileversion"></span>**DXFILEERR\_BADFILEVERSION**
</dt> <dd>

File version is not valid.

</dd> <dt>

<span id="DXFILEERR_BADINTRINSICS"></span><span id="dxfileerr_badintrinsics"></span>**DXFILEERR\_BADINTRINSICS**
</dt> <dd>

Intrinsics are invalid.

</dd> <dt>

<span id="DXFILEERR_BADOBJECT"></span><span id="dxfileerr_badobject"></span>**DXFILEERR\_BADOBJECT**
</dt> <dd>

Object is invalid.

</dd> <dt>

<span id="DXFILEERR_BADRESOURCE"></span><span id="dxfileerr_badresource"></span>**DXFILEERR\_BADRESOURCE**
</dt> <dd>

Resource is invalid.

</dd> <dt>

<span id="DXFILEERR_BADSTREAMHANDLE"></span><span id="dxfileerr_badstreamhandle"></span>**DXFILEERR\_BADSTREAMHANDLE**
</dt> <dd>

Stream handle is invalid.

</dd> <dt>

<span id="DXFILEERR_BADTYPE"></span><span id="dxfileerr_badtype"></span>**DXFILEERR\_BADTYPE**
</dt> <dd>

Object type is invalid.

</dd> <dt>

<span id="DXFILEERR_BADVALUE"></span><span id="dxfileerr_badvalue"></span>**DXFILEERR\_BADVALUE**
</dt> <dd>

Parameter is invalid.

</dd> <dt>

<span id="DXFILEERR_FILENOTFOUND"></span><span id="dxfileerr_filenotfound"></span>**DXFILEERR\_FILENOTFOUND**
</dt> <dd>

File could not be found.

</dd> <dt>

<span id="DXFILEERR_INTERNALERROR"></span><span id="dxfileerr_internalerror"></span>**DXFILEERR\_INTERNALERROR**
</dt> <dd>

Internal error occurred.

</dd> <dt>

<span id="DXFILEERR_NOINTERNET"></span><span id="dxfileerr_nointernet"></span>**DXFILEERR\_NOINTERNET**
</dt> <dd>

Internet connection not found.

</dd> <dt>

<span id="DXFILEERR_NOMOREDATA"></span><span id="dxfileerr_nomoredata"></span>**DXFILEERR\_NOMOREDATA**
</dt> <dd>

No further data is available.

</dd> <dt>

<span id="DXFILEERR_NOMOREOBJECTS"></span><span id="dxfileerr_nomoreobjects"></span>**DXFILEERR\_NOMOREOBJECTS**
</dt> <dd>

All objects have been enumerated.

</dd> <dt>

<span id="DXFILEERR_NOMORESTREAMHANDLES"></span><span id="dxfileerr_nomorestreamhandles"></span>**DXFILEERR\_NOMORESTREAMHANDLES**
</dt> <dd>

No stream handles are available.

</dd> <dt>

<span id="DXFILEERR_NOTDONEYET"></span><span id="dxfileerr_notdoneyet"></span>**DXFILEERR\_NOTDONEYET**
</dt> <dd>

Operation has not completed.

</dd> <dt>

<span id="DXFILEERR_NOTFOUND"></span><span id="dxfileerr_notfound"></span>**DXFILEERR\_NOTFOUND**
</dt> <dd>

Object could not be found.

</dd> <dt>

<span id="DXFILEERR_PARSEERROR"></span><span id="dxfileerr_parseerror"></span>**DXFILEERR\_PARSEERROR**
</dt> <dd>

File could not be parsed.

</dd> <dt>

<span id="DXFILEERR_RESOURCENOTFOUND"></span><span id="dxfileerr_resourcenotfound"></span>**DXFILEERR\_RESOURCENOTFOUND**
</dt> <dd>

Resource could not be found.

</dd> <dt>

<span id="DXFILEERR_NOTEMPLATE"></span><span id="dxfileerr_notemplate"></span>**DXFILEERR\_NOTEMPLATE**
</dt> <dd>

No template available.

</dd> <dt>

<span id="DXFILEERR_URLNOTFOUND"></span><span id="dxfileerr_urlnotfound"></span>**DXFILEERR\_URLNOTFOUND**
</dt> <dd>

URL could not be found.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DXFile.h</dt> </dl> |



## See also

<dl> <dt>

[X File Reference (Legacy)](dx9-graphics-reference-x-file.md)
</dt> </dl>

 

 





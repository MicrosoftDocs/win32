---
UID: NF:directml.DMLCreateDevice1
title: DMLCreateDevice1 function
description: Creates a DirectML device for a given Direct3D 12 device.
helpviewer_keywords: ["DMLCreateDevice1","DMLCreateDevice1 function","direct3d12.dmlcreatedevice1","directml/DMLCreateDevice1"]
ms.topic: reference
tech.root: directml
ms.date: 11/04/2020
req.header: directml.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: DirectML.lib
req.dll: DirectML.dll
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - DMLCreateDevice1
 - directml/DMLCreateDevice1
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - DirectML.dll
api_name:
 - DMLCreateDevice1
---

# DMLCreateDevice1 function (directml.h)

Creates a DirectML device for a given Direct3D 12 device.

> [!IMPORTANT]
> This API is available as part of the DirectML standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/) version 1.4 and later. Also see [DirectML version history](../dml-version-history.md).

## Syntax

```cpp
HRESULT DMLCreateDevice1(
  ID3D12Device            *d3d12Device,
  DML_CREATE_DEVICE_FLAGS flags,
  DML_FEATURE_LEVEL       minimumFeatureLevel,
  REFIID                  riid,
  void                    **ppv
);
```

## Parameters

`d3d12Device`

Type: <b><a href="/windows/win32/api/d3d12/nn-d3d12-id3d12device">ID3D12Device</a>*</b>

A pointer to an [ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device) representing the Direct3D 12 device to create the DirectML device over. DirectML supports any D3D feature level, and Direct3D 12 devices created on any adapter, including WARP. However, not all features in DirectML may be available depending on the capabilities of the Direct3D 12 device. See [IDMLDevice::CheckFeatureSupport](/windows/win32/api/directml/nf-directml-idmldevice-checkfeaturesupport) for more info.

If the call to **DMLCreateDevice1** is successful, then the DirectML device maintains a strong reference to the supplied Direct3D 12 device.

`flags`

Type: <b>DML_CREATE_DEVICE_FLAGS</b>

A [DML_CREATE_DEVICE_FLAGS](/windows/win32/api/directml/ne-directml-dml_create_device_flags) value specifying additional device creation options.

`minimumFeatureLevel`

Type: <b>DML_FEATURE_LEVEL</b>

A [DML_FEATURE_LEVEL](/windows/win32/api/directml/ne-directml-dml_feature_level) value specifying the minimum feature level support required.

This parameter can be useful for callers that require a specific version of DirectML, but who may find themselves calling into an older version of DirectML. This can happen, for example, when the user runs your application on an older version of Windows 10.

Applications that explicitly depend on functionality introduced in a particular feature level can specify it as a *minimumFeatureLevel*. This will guarantee that **DMLCreateDevice1** won't succeed unless the underlying implementation is *at least* as capable as this requested minimum feature level.

Note that as this parameter specifies a *minimum* feature level, the underlying DirectML device may in fact support a higher feature level than the requested minimum. Once device creation succeeds, you can query all of the feature levels supported by this device using [IDMLDevice::CheckFeatureSupport](/windows/win32/api/directml/nf-directml-idmldevice-checkfeaturesupport).

`riid`

Type: <b>REFIID</b>

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in <i>device</i>. This is expected to be the GUID of [IDMLDevice](/windows/win32/api/directml/nn-directml-idmldevice).

`ppv`

Type: \_COM\_Outptr\_opt\_ <b>void**</b>

A pointer to a memory block that receives a pointer to the device. This is the address of a pointer to an [IDMLDevice](/windows/win32/api/directml/nn-directml-idmldevice), representing  the DirectML device created.


## Return value

Type: [**HRESULT**](/windows/desktop/winprog/windows-data-types)

If the function succeeds, it returns <b>S_OK</b>. Otherwise, it returns an [HRESULT](/windows/desktop/winprog/windows-data-types) error code.

If this version of DirectML doesn't support the *minimumFeatureLevel* requested, then this function will return **DXGI_ERROR_UNSUPPORTED**.

The Graphics Tools Feature on Demand (FOD) must be installed in order to use the DirectML debug layers. If the [DML_CREATE_DEVICE_FLAG_DEBUG](/windows/win32/api/directml/ne-directml-dml_create_device_flags) flag is specified in *flags* and the debug layers are not installed, then **DMLCreateDevice1** returns **DXGI_ERROR_SDK_COMPONENT_MISSING**.

## Remarks

A newer version of this function, [DMLCreateDevice1](), was introduced in DirectML version 1.1.0. **DMLCreateDevice1** is equivalent to calling **DMLCreateDevice1** and supplying a *minimumFeatureLevel* of [DML_FEATURE_LEVEL_1_0](/windows/win32/api/directml/ne-directml-dml_feature_level).

## Availability

This API was introduced in DirectML version `1.1.0`.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | directml.h |
| **Library** | DirectML.lib |
| **DLL** | DirectML.dll |

## See also

* [DML_FEATURE_LEVEL enumeration](/windows/win32/api/directml/ne-directml-dml_feature_level)
* [DirectML version history](../dml-version-history.md)
* [DirectML feature level history](/windows/win32/direct3d12/dml-feature_level-history)    
* [Using the DirectML debug layer](../dml-debug-layer.md)
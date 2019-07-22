---
title: Binding in DirectML
description: The DirectML debug layer is an optional development-time component that helps you in debugging your DirectML code.
ms.custom: Windows 10 May 2019 Update
ms.localizationpriority: high
ms.topic: article
ms.date: 04/19/2019
---

# Using the DirectML debug layer

The DirectML debug layer is an optional development-time component that helps you in debugging your DirectML code. The debug layer is part of a separate Graphics Tools package, distributed as a [Feature-on-Demand](/windows-hardware/manufacture/desktop/features-on-demand-v2--capabilities) (FOD). The Graphics Tools FOD must be installed on your system in order to use the debug layer.

We highly recommended that you enable the debug layer while developing applications using DirectML, because it can provide invaluable information in the event of invalid API usage.

## Installing the DirectML debug layer

To install the optional Graphics Tools feature-on-demand (FOD) package, run the following command from an administrator Powershell prompt.

```powershell
Add-WindowsCapability -Online -Name "Tools.Graphics.DirectX~~~~0.0.1.0"
```

Alternatively, you can install the Graphics Tools package from within Windows 10 Settings. Navigate to **Settings** > **Apps** > **Apps & features** > **Optional features** > **Add a feature** > then select **Graphics Tools**.

## Enabling the DirectML debug layer

Once the Graphics Tools package is installed, you can enable the DirectML debug layer by supplying  [**DML_CREATE_DEVICE_FLAG_DEBUG**](/windows/desktop/api/directml/ne-directml-dml_create_device_flag) when you call [**DMLCreateDevice**](/windows/desktop/api/directml/nf-directml-dmlcreatedevice.md).

> [!IMPORTANT]
> You must first enable the Direct3D 12 debug layer. And *then* enable the DirectML debug layer by calling **DMLCreateDevice**.

Once you've enabled the DirectML debug layer, any DirectML errors or invalid API calls will cause debugging information to be emitted as debug output. Here's an example.

```console
DML_OPERATOR_CONVOLUTION: invalid D3D12_HEAP_TYPE. DirectML requires all bound buffers to be D3D12_HEAP_TYPE_DEFAULT.
```

## See also

* [DMLCreateDevice function](/windows/desktop/api/directml/nf-directml-dmlcreatedevice.md)
* [Available Features-on-Demand](/windows-hardware/manufacture/desktop/features-on-demand-non-language-fod)
* [Use GPU-based validation with the Direct3D 12 Debug Layer](/windows/desktop/direct3d12/using-d3d12-debug-layer-gpu-based-validation)
* [Direct3D 12 Debug Layer reference](/windows/desktop/direct3d12/direct3d-12-sdklayers-reference)

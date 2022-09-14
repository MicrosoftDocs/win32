---
title: DXCoreAdapterProperty
description: Defines constants that specify DXCore adapter properties.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreAdapterProperty enum

Defines constants that specify DXCore adapter properties. Pass one of these constants to the [IDXCoreAdapter::GetPropertySize](./nf-dxcore_interface-idxcoreadapter-getpropertysize.md) method to retrieve the buffer size necessary to receive the value of the corresponding property; then pass the same constant to the [IDXCoreAdapter::GetProperty](./nf-dxcore_interface-idxcoreadapter-getproperty.md) method to retrieve the property's value in a buffer that you allocate.

## Syntax

```cpp
enum class DXCoreAdapterProperty : uint32_t
{
  InstanceLuid = 0,
  DriverVersion = 1,
  DriverDescription = 2,
  HardwareID = 3,
  KmdModelVersion = 4,
  ComputePreemptionGranularity = 5,
  GraphicsPreemptionGranularity = 6,
  DedicatedAdapterMemory = 7,
  DedicatedSystemMemory = 8,
  SharedSystemMemory = 9,
  AcgCompatible = 10,
  IsHardware = 11,
  IsIntegrated = 12,
  IsDetachable = 13
};
```

## Constants

### InstanceLuid

Specifies the <em>InstanceLuid</em> adapter property, which contains a locally unique identifier representing the adapter. This value remains constant for the lifetime of this adapter. The LUID of an adapter changes on reboot, driver upgrade, or device disablement/enablement.

The <em>InstanceLuid</em> adapter property has type <a href="/windows/win32/api/winnt/ns-winnt-luid">LUID</a>.

### DriverVersion

Specifies the <em>DriverVersion</em> adapter property, which contains the driver version, represented in <b>WORD</b>s as a <b>LARGE_INTEGER</b>.

The <em>DriverVersion</em> adapter property has type <b>uint64_t</b>, representing a Boolean value.

### DriverDescription

Specifies the <em>DriverDescription</em> adapter property, which contains a NULL-terminated array of <b>CHAR</b>s describing the driver, as specified by the driver, in <a href="/windows/win32/intl/unicode">UTF-8</a> encoding.

The <em>DriverDescription</em> adapter property has type <b>char*</b>.

### HardwareID

Specifies the <em>HardwareID</em> adapter property, which represents the PnP hardware ID parts.

The <em>HardwareID</em> adapter property has type <a href="/windows/win32/dxcore/dxcore_interface/ns-dxcore_interface-dxcorehardwareid">DXCoreHardwareID</a>.

### KmdModelVersion

Specifies the <em>KmdModelVersion</em> adapter property, which represents the driver model.

The <em>KmdModelVersion</em> adapter property has type <a href="/windows-hardware/drivers/ddi/content/d3dkmthk/ne-d3dkmthk-_qai_driverversion">D3DKMT_DRIVERVERSION</a>.

### ComputePreemptionGranularity

Specifies the <em>ComputePreemptionGranularity</em> adapter property, which represents the compute preemption granularity.

The <em>ComputePreemptionGranularity</em> adapter property has type <b>uint16_t</b>, representing a <a href="/windows-hardware/drivers/ddi/content/d3dkmdt/ne-d3dkmdt-_d3dkmdt_compute_preemption_granularity">D3DKMDT_COMPUTE_PREEMPTION_GRANULARITY</a> value.

### GraphicsPreemptionGranularity

Specifies the <em>GraphicsPreemptionGranularity</em> adapter property, which represents the graphics preemption granularity.

The <em>GraphicsPreemptionGranularity</em> adapter property has type <b>uint16_t</b>, representing a <a href="/windows-hardware/drivers/ddi/content/d3dkmdt/ne-d3dkmdt-_d3dkmdt_graphics_preemption_granularity">D3DKMDT_GRAPHICS_PREEMPTION_GRANULARITY</a> value.

### DedicatedAdapterMemory

Specifies the <em>DedicatedAdapterMemory</em> adapter property, which represents the number of bytes of dedicated adapter memory that are not shared with the CPU.

The <em>DedicatedVideoMemory</em> adapter property has type <b>uint64_t</b>.

### DedicatedSystemMemory

Specifies the <em>DedicatedSystemMemory</em> adapter property, which represents the number of bytes of dedicated system memory that are not shared with the CPU. This memory is allocated from available system memory at boot time.

The <em>DedicatedSystemMemory</em> adapter property has type <b>uint64_t</b>.

### SharedSystemMemory

Specifies the <em>SharedSystemMemory</em> adapter property, which represents the number of bytes of shared system memory. This is the maximum value of system memory that may be consumed by the adapter during operation. Any incidental memory consumed by the driver as it manages and uses video memory is additional.

The <em>SharedSystemMemory</em> adapter property has type <b>uint64_t</b>.

### AcgCompatible

Specifies the <em>AcgCompatible</em> adapter property, which indicates whether the adapter is compatible with processes that enforce Arbitrary Code Guard.

The <em>AcgCompatible</em> adapter property has type <b>bool</b>.

### IsHardware

Specifies the <em>IsHardware</em> adapter property, which determines whether or not this is a hardware adapter. An adapter that's not a hardware adapter is a software adapter.

The <em>IsHardware</em> adapter property has type <b>bool</b>.

### IsIntegrated

Specifies the <em>IsIntegrated</em> adapter property, which determines whether the adapter is reported to be an integrated graphics processor (iGPU).

The <em>IsIntegrated</em> adapter property has type <b>bool</b>.

### IsDetachable

Specifies the <em>IsDetachable</em> adapter property, which determines whether the adapter has been reported to be detachable, or removable.

The <em>IsDetachable</em> adapter property has type <b>bool</b>.

<b>Note</b>. Even if <a href="/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getproperty">IDXCoreAdapter::GetProperty</a> indicates `false` for this property, the adapter still has the ability to be reported as removed, such as in the case of malfunction, or driver update.

## See also

[IDXCoreAdapter::GetPropertySize](./nf-dxcore_interface-idxcoreadapter-getpropertysize.md), [IDXCoreAdapter::GetProperty](./nf-dxcore_interface-idxcoreadapter-getproperty.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

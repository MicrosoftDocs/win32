---
title: STOR\_POFX\_COMPONENT structure
description: The STOR\_POFX\_COMPONENT structure describes the power state attributes of a storage device component.
ms.assetid: 'D44FF0C7-D82C-4CDD-A5F9-BBD8257C6771'
keywords: ["STOR_POFX_COMPONENT structure Storage Devices", "PSTOR_POFX_COMPONENT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_POFX_COMPONENT
api_location:
- storport.h
api_type:
- HeaderDef
---

# STOR\_POFX\_COMPONENT structure

The **STOR\_POFX\_COMPONENT** structure describes the power state attributes of a storage device component.

## Syntax


```C++
typedef struct _PO_FX_COMPONENT {
  ULONG                          Version;
  USHORT                         Size;
  ULONG                          FStateCount;
  ULONG                          DeepestWakeableIdleState;
  GUID                           Id;
  STOR_POFX_COMPONENT_IDLE_STATE FStates[ANYSIZE_ARRAY];
} STOR_POFX_COMPONENT, *PSTOR_POFX_COMPONENT;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number of this structure. Set this member to **STOR\_POFX\_DEVICE\_VERSION\_V1**.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set this value to **STOR\_POFX\_COMPONENT\_SIZE**.

</dd> <dt>

**FStateCount**
</dt> <dd>

The number of elements in the array that is pointed to by the **FStates** member. Additionally, this member specifies the number of functional power states (F-state) that the component supports. A component must support at least one F-state (F0).

</dd> <dt>

**DeepestWakeableIdleState**
</dt> <dd>

The index of the deepest F-state from which the component can wake. Specify 0 for F0, 1 for F1, and so on. This index must be less than **FStateCount**.

</dd> <dt>

**Id**
</dt> <dd>

A component ID that uniquely identifies this component with respect to the other components in the device. The driver should specify a nonzero value for this member if the power management framework (PoFx) requires a component ID to distinguish this component from other, similar components in the same device. The component IDs supported by Storport are STORPORT\_POFX\_ADAPTER\_GUID and STORPORT\_POFX\_LUN\_GUID.

</dd> <dt>

**FStates**
</dt> <dd>

A array of [**STOR\_POFX\_COMPONENT\_IDLE\_STATE**](stor-pofx-component-idle-state.md) structures. The length of this array is specified by the **FStateCount** member. Each array element specifies the attributes of an F-state that is supported by the component. Element 0 describes F0, element 1 describes F1, and so on. When more than one idle state structure is required, the additional structures are allocated at the end of the **STOR\_ POFX\_COMPONENT** structure and the **FStateCount** is set to 1, the value of ANYSIZE\_ARRAY, plus the count of the additional structures.

</dd> </dl>

## Remarks

When a miniport driver registers a device with the Storport power management framework, the miniport driver supplies a [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure that holds the registration information. This structure contains an array of **STOR\_ POFX\_COMPONENT** structures. The elements in this array describe the power attributes of the individual components in the device. The power settings of these components are managed based on the information in this array.

The **Id** member contains a component ID that uniquely identifies a component. The component ID is not the same as the component index, which a routine such as [**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md) uses to identify a component in a registered device. A component index is an index into the **Components** array in the [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure that the device driver used to register the device. If the **Components** array contains N elements, component indexes are integer values in the range 0 to N–1. In contrast, a component ID is a GUID value.

The ID for the single adapter device component is defined in *storport.h* as STORPORT\_POFX\_ADAPTER\_GUID. The ID for the single unit device component is STORPORT\_POFX\_LUN\_GUID. Use these identifiers when describing either an adapter component or a unit component in the **Id** member.

For a adapter device component, a maximum of one F-state (F0) is permitted. For a unit device component, two F-states are allowed. The unit device must have the F0 state specified and optionally have one additional F-state.

For a unit device component, if an additional F-state is included in the **FStates** array, the size member remains set to **STOR\_POFX\_COMPONENT\_SIZE** and does not include the size of the additional [**STOR\_POFX\_COMPONENT\_IDLE\_STATE**](stor-pofx-component-idle-state.md) structure.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Supported starting with Windows 8.<br/>                                         |
| Header<br/>  | <dl> <dt>Storport.h</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_POFX\_COMPONENT\_IDLE\_STATE**](stor-pofx-component-idle-state.md)
</dt> <dt>

[**STOR\_POFX\_DEVICE**](stor-pofx-device.md)
</dt> <dt>

[**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_POFX_COMPONENT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







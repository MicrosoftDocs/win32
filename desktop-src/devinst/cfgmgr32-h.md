---
title: Cfgmgr32.h
description: This section contains reference topics for the Cfgmgr32.h header.
ms.assetid: '73b4b2ec-ce3d-47c1-9b0e-1052f390ae94'
---

# Cfgmgr32.h

This section contains reference topics for the Cfgmgr32.h header.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>BUSNUMBER_DES</strong>](busnumber-des.md)<br/></td>
<td>The BUSNUMBER_DES structure is used for specifying either a resource list or a resource requirements list that describes bus number usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>BUSNUMBER_RANGE</strong>](busnumber-range.md)<br/></td>
<td>The BUSNUMBER_RANGE structure specifies a resource requirements list that describes bus number usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BUSNUMBER_RESOURCE</strong>](busnumber-resource.md)<br/></td>
<td>The BUSNUMBER_RESOURCE structure specifies either a resource list or a resource requirements list that describes bus number usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_Empty_Log_Conf</strong>](cm-add-empty-log-conf.md)<br/></td>
<td>The <strong>CM_Add_Empty_Log_Conf</strong> function creates an empty [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), for a specified configuration type and a specified device instance, on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_Empty_Log_Conf_Ex</strong>](cm-add-empty-log-conf-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_Empty_Log_Conf</strong>](cm-add-empty-log-conf.md) instead.
</blockquote>
<br/> The <strong>CM_Add_Empty_Log_Conf_Ex</strong> function creates an empty [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), for a specified configuration type and a specified device instance, on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_ID</strong>](cm-add-id.md)<br/></td>
<td>The <strong>CM_Add_ID</strong> function appends a specified [device ID](https://msdn.microsoft.com/library/windows/hardware/ff541237) (if not already present) to a [device instance's](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) [hardware ID](https://msdn.microsoft.com/library/windows/hardware/ff546152) list or [compatible ID](https://msdn.microsoft.com/library/windows/hardware/ff539950) list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_ID_Ex</strong>](cm-add-id-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_ID</strong>](cm-add-id.md) instead.
</blockquote>
<br/> The <strong>CM_Add_ID_Ex</strong> function appends a [device ID](https://msdn.microsoft.com/library/windows/hardware/ff541237) (if not already present) to a device instance's [hardware ID](https://msdn.microsoft.com/library/windows/hardware/ff546152) list or [compatible ID](https://msdn.microsoft.com/library/windows/hardware/ff539950) list, on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_Res_Des</strong>](cm-add-res-des.md)<br/></td>
<td>The <strong>CM_Add_Res_Des</strong> function adds a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) to a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_Res_Des_Ex</strong>](cm-add-res-des-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_Res_Des</strong>](cm-add-res-des.md) instead.
</blockquote>
<br/> The <strong>CM_Add_Res_Des_Ex</strong> function adds a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) to a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg). The logical configuration can be on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Connect_Machine</strong>](cm-connect-machine.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning in Windows 8 and Windows Server 2012 functionality to access remote machines has been removed. You cannot access remote machines when running on these versions of Windows.
</blockquote>
<br/> The <strong>CM_Connect_Machine</strong> function creates a connection to a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_Class_Key</strong>](cm-delete-class-key.md)<br/></td>
<td>The <strong>CM_Delete_Class_Key</strong> function removes the specified installed [device class](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class) from the system.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Delete_Device_Interface_Key</strong>](cm-delete-device-interface-key.md)<br/></td>
<td>The <strong>CM_Delete_Device_Interface_Key</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_Device_Interface_Key_ExA</strong>](cm-delete-device-interface-key-exa.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Delete_Device_Interface_Key</strong>](cm-delete-device-interface-key.md) instead.
</blockquote>
<br/> The <strong>CM_Delete_Device_Interface_Key_ExA</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Delete_Device_Interface_Key_ExW</strong>](cm-delete-device-interface-key-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Delete_Device_Interface_Key</strong>](cm-delete-device-interface-key.md) instead.
</blockquote>
<br/> The <strong>CM_Delete_Device_Interface_Key_ExW</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_DevNode_Key</strong>](cm-delete-devnode-key.md)<br/></td>
<td>The <strong>CM_Delete_DevNode_Key</strong> function deletes the specified user-accessible registry keys that are associated with a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Disable_DevNode</strong>](cm-disable-devnode.md)<br/></td>
<td>The <strong>CM_Disable_DevNode</strong> function disables a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Disconnect_Machine</strong>](cm-disconnect-machine.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning in Windows 8 and Windows Server 2012 functionality to access remote machines has been removed. You cannot access remote machines when running on these versions of Windows.
</blockquote>
<br/> The <strong>CM_Disconnect_Machine</strong> function removes a connection to a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enable_DevNode</strong>](cm-enable-devnode.md)<br/></td>
<td>The <strong>CM_Enable_DevNode</strong> function enables a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Enumerate_Classes</strong>](cm-enumerate-classes.md)<br/></td>
<td>The <strong>CM_Enumerate_Classes</strong> function, when called repeatedly, enumerates the local machine's installed [device classes](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class) by supplying each class's GUID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enumerate_Classes_Ex</strong>](cm-enumerate-classes-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Enumerate_Classes</strong>](cm-enumerate-classes.md) instead.
</blockquote>
<br/> The <strong>CM_Enumerate_Classes_Ex</strong> function, when called repeatedly, enumerates a local or a remote machine's installed [device classes](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class), by supplying each class's GUID.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Enumerate_Enumerators</strong>](cm-enumerate-enumerators.md)<br/></td>
<td>The <strong>CM_Enumerate_Enumerators</strong> function enumerates the local machine's device enumerators by supplying each enumerator's name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enumerate_Enumerators_Ex</strong>](cm-enumerate-enumerators-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Enumerate_Enumerators</strong>](cm-enumerate-enumerators.md) instead.
</blockquote>
<br/> The <strong>CM_Enumerate_Enumerators_Ex</strong> function enumerates a local or a remote machine's device enumerators, by supplying each enumerator's name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Log_Conf</strong>](cm-free-log-conf.md)<br/></td>
<td>The <strong>CM_Free_Log_Conf</strong> function removes a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) and all associated [resource descriptors](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Log_Conf_Ex</strong>](cm-free-log-conf-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Free_Log_Conf</strong>](cm-free-log-conf.md) instead.
</blockquote>
<br/> The <strong>CM_Free_Log_Conf_Ex</strong> function removes a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) and all associated [resource descriptors](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from either a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Log_Conf_Handle</strong>](cm-free-log-conf-handle.md)<br/></td>
<td>The <strong>CM_Free_Log_Conf_Handle</strong> function invalidates a logical configuration handle and frees its associated memory allocation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Res_Des</strong>](cm-free-res-des.md)<br/></td>
<td>The <strong>CM_Free_Res_Des</strong> function removes a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Res_Des_Ex</strong>](cm-free-res-des-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Free_Res_Des</strong>](cm-free-res-des.md) instead.
</blockquote>
<br/> The <strong>CM_Free_Res_Des_Ex</strong> function removes a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on either a local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Res_Des_Handle</strong>](cm-free-res-des-handle.md)<br/></td>
<td>The <strong>CM_Free_Res_Des_Handle</strong> function invalidates a resource description handle and frees its associated memory allocation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Resource_Conflict_Handle</strong>](cm-free-resource-conflict-handle.md)<br/></td>
<td>The <strong>CM_Free_Resource_Conflict_Handle</strong> function invalidates a handle to a resource conflict list, and frees the handle's associated memory allocation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Child</strong>](cm-get-child.md)<br/></td>
<td>The <strong>CM_Get_Child</strong> function is used to retrieve a device instance handle to the first child node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Child_Ex</strong>](cm-get-child-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Child</strong>](cm-get-child.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Child_Ex</strong> function is used to retrieve a device instance handle to the first child node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Property</strong>](cm-get-class-property.md)<br/></td>
<td>The <strong>CM_Get_Class_Property</strong> function retrieves a device property that is set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Class_Property_ExW</strong>](cm-get-class-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Class_Property</strong>](cm-get-class-property.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Class_Property_ExW</strong> function retrieves a device property that is set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Property_Keys</strong>](cm-get-class-property-keys.md)<br/></td>
<td>The <strong>CM_Get_Class_Property_Keys</strong> function retrieves an array of the device property keys that represent the device properties that are set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Class_Property_Keys_Ex</strong>](cm-get-class-property-keys-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Class_Property_Keys</strong>](cm-get-class-property-keys.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Class_Property_Keys_Ex</strong> function retrieves an array of the device property keys that represent the device properties that are set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Registry_Property</strong>](cm-get-class-registry-property.md)<br/></td>
<td>The <strong>CM_Get_Class_Registry_Property</strong> function retrieves a [device setup class property](https://msdn.microsoft.com/library/windows/hardware/ff537744).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Depth</strong>](cm-get-depth.md)<br/></td>
<td>The <strong>CM_Get_Depth</strong> function is used to obtain the depth of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) within the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Depth_Ex</strong>](cm-get-depth-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Depth</strong>](cm-get-depth.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Depth_Ex</strong> function is used to obtain the depth of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) within a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID</strong>](cm-get-device-id.md)<br/></td>
<td>The <strong>CM_Get_Device_ID</strong> function retrieves the [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_Ex</strong>](cm-get-device-id-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID</strong>](cm-get-device-id.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_Ex</strong> function retrieves the [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_List</strong>](cm-get-device-id-list.md)<br/></td>
<td>The <strong>CM_Get_Device_ID_List</strong> function retrieves a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the local computer's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_List_Ex</strong>](cm-get-device-id-list-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_List</strong>](cm-get-device-id-list.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_List_Ex</strong> function retrieves a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_List_Size</strong>](cm-get-device-id-list-size.md)<br/></td>
<td>The <strong>CM_Get_Device_ID_List_Size</strong> function retrieves the buffer size required to hold a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the local machine's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_List_Size_Ex</strong>](cm-get-device-id-list-size-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_List_Size</strong>](cm-get-device-id-list-size.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_List_Size_Ex</strong> function retrieves the buffer size required to hold a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a local or a remote machine's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_Size</strong>](cm-get-device-id-size.md)<br/></td>
<td>The <strong>CM_Get_Device_ID_Size</strong> function retrieves the buffer size required to hold a [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_Size_Ex</strong>](cm-get-device-id-size-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_Size</strong>](cm-get-device-id-size.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_Size_Ex</strong> function retrieves the buffer size required to hold a [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Alias</strong>](cm-get-device-interface-alias.md)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Alias</strong> function returns the alias of the specified device interface instance, if the alias exists.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_List</strong>](cm-get-device-interface-list.md)<br/></td>
<td>The <strong>CM_Get_Device_Interface_List</strong> function retrieves a list of device interface instances that belong to a specified [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_List_Size</strong>](cm-get-device-interface-list-size.md)<br/></td>
<td>The <strong>CM_Get_Device_Interface_List_Size</strong> function retrieves the buffer size that must be passed to the [<strong>CM_Get_Device_Interface_List</strong>](cm-get-device-interface-list.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_Property</strong>](cm-get-device-interface-property.md)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Property</strong> function retrieves a device property that is set for a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Property_ExW</strong>](cm-get-device-interface-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_Interface_Property</strong>](cm-get-device-interface-property.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_Interface_Property_ExW</strong> function retrieves a device property that is set for a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_Property_Keys</strong>](cm-get-device-interface-property-keys.md)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Property_Keys</strong> function retrieves an array of device property keys that represent the device properties that are set for a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Property_Keys_ExW</strong>](cm-get-device-interface-property-keys-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_Interface_Property_Keys</strong>](cm-get-device-interface-property-keys.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_Interface_Property_Keys_ExW</strong> function retrieves an array of device property keys that represent the device properties that are set for a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Property</strong>](cm-get-devnode-property.md)<br/></td>
<td>The <strong>CM_Get_DevNode_Property</strong> function retrieves a device instance property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Property_ExW</strong>](cm-get-devnode-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Property</strong>](cm-get-devnode-property.md) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Property_ExW</strong> function retrieves a device instance property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Property_Keys</strong>](cm-get-devnode-property-keys.md)<br/></td>
<td>The <strong>CM_Get_DevNode_Property_Keys</strong> function retrieves an array of the device property keys that represent the device properties that are set for a device instance.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Property_Keys_Ex</strong>](cm-get-devnode-property-keys-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Property_Keys</strong>](cm-get-devnode-property-keys.md) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Property_Keys_Ex</strong> function retrieves an array of the device property keys that represent the device properties that are set for a device instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Registry_Property</strong>](cm-get-devnode-registry-property.md)<br/></td>
<td>The <strong>CM_Get_DevNode_Registry_Property</strong> function retrieves a specified device property from the registry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Status</strong>](cm-get-devnode-status.md)<br/></td>
<td>The <strong>CM_Get_DevNode_Status</strong> function obtains the status of a device instance from its device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Status_Ex</strong>](cm-get-devnode-status-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Status</strong>](cm-get-devnode-status.md) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Status_Ex</strong> function obtains the status of a device instance from its device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) on a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_First_Log_Conf</strong>](cm-get-first-log-conf.md)<br/></td>
<td>The <strong>CM_Get_First_Log_Conf</strong> function obtains the first [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), of a specified configuration type, associated with a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_First_Log_Conf_Ex</strong>](cm-get-first-log-conf-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_First_Log_Conf</strong>](cm-get-first-log-conf.md) instead.
</blockquote>
<br/> The <strong>CM_Get_First_Log_Conf_Ex</strong> function obtains the first [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_HW_Prof_Flags</strong>](cm-get-hw-prof-flags.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_HW_Prof_Flags</strong> function retrieves the [hardware profile](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-profile)-specific configuration flags for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_HW_Prof_Flags_Ex</strong>](cm-get-hw-prof-flags-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
This function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_HW_Prof_Flags_Ex</strong> function retrieves the [hardware profile](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-profile)-specific configuration flags for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a remote machine or a local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Log_Conf_Priority</strong>](cm-get-log-conf-priority.md)<br/></td>
<td>The <strong>CM_Get_Log_Conf_Priority</strong> function obtains the configuration priority of a specified [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Log_Conf_Priority_Ex</strong>](cm-get-log-conf-priority-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Log_Conf_Priority</strong>](cm-get-log-conf-priority.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Log_Conf_Priority_Ex</strong> function obtains the configuration priority of a specified [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Next_Log_Conf</strong>](cm-get-next-log-conf.md)<br/></td>
<td>The <strong>CM_Get_Next_Log_Conf</strong> function obtains the next [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specific [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Next_Log_Conf_Ex</strong>](cm-get-next-log-conf-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Next_Log_Conf</strong>](cm-get-next-log-conf.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Next_Log_Conf_Ex</strong> function obtains the next [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specific [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Next_Res_Des</strong>](cm-get-next-res-des.md)<br/></td>
<td>The <strong>CM_Get_Next_Res_Des</strong> function obtains a handle to the next [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor), of a specified resource type, for a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Next_Res_Des_Ex</strong>](cm-get-next-res-des-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Next_Res_Des</strong>](cm-get-next-res-des.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Next_Res_Des_Ex</strong> function obtains a handle to the next [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor), of a specified resource type, for a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Parent</strong>](cm-get-parent.md)<br/></td>
<td>The <strong>CM_Get_Parent</strong> function obtains a device instance handle to the parent node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's device tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Parent_Ex</strong>](cm-get-parent-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Parent</strong>](cm-get-parent.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Parent_Ex</strong> function obtains a device instance handle to the parent node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Res_Des_Data</strong>](cm-get-res-des-data.md)<br/></td>
<td>The <strong>CM_Get_Res_Des_Data</strong> function retrieves the information stored in a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Res_Des_Data_Ex</strong>](cm-get-res-des-data-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Res_Des_Data</strong>](cm-get-res-des-data.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Res_Des_Data_Ex</strong> function retrieves the information stored in a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Res_Des_Data_Size</strong>](cm-get-res-des-data-size.md)<br/></td>
<td>The <strong>CM_Get_Res_Des_Data_Size</strong> function obtains the buffer size required to hold the information contained in a specified [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Res_Des_Data_Size_Ex</strong>](cm-get-res-des-data-size-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Res_Des_Data_Size</strong>](cm-get-res-des-data-size.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Res_Des_Data_Size_Ex</strong> function obtains the buffer size required to hold the information contained in a specified [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Resource_Conflict_Count</strong>](cm-get-resource-conflict-count.md)<br/></td>
<td>The <strong>CM_Get_Resource_Conflict_Count</strong> function obtains the number of conflicts contained in a specified resource conflict list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Resource_Conflict_Details</strong>](cm-get-resource-conflict-details.md)<br/></td>
<td>The <strong>CM_Get_Resource_Conflict_Details</strong> function obtains the details about one of the resource conflicts in a conflict list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Sibling</strong>](cm-get-sibling.md)<br/></td>
<td>The <strong>CM_Get_Sibling</strong> function obtains a device instance handle to the next sibling node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Sibling_Ex</strong>](cm-get-sibling-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Sibling</strong>](cm-get-sibling.md) instead.
</blockquote>
<br/> The <strong>CM_Get_Sibling_Ex</strong> function obtains a device instance handle to the next sibling node of a specified device node, in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Version</strong>](cm-get-version.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_Version</strong> function returns version 4.0 of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) for a local machine. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Version_Ex</strong>](cm-get-version-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_Version_Ex</strong> function returns version 4.0 of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) for a local or a remote machine. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Is_Dock_Station_Present</strong>](cm-is-dock-station-present.md)<br/></td>
<td>The <strong>CM_Is_Dock_Station_Present</strong> function identifies whether a [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station) is present in a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Is_Dock_Station_Present_Ex</strong>](cm-is-dock-station-present-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Is_Dock_Station_Present</strong>](cm-is-dock-station-present.md) instead.
</blockquote>
<br/> The <strong>CM_Is_Dock_Station_Present_Ex</strong> function identifies whether a [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station) is present in a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Is_Version_Available</strong>](cm-is-version-available.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Is_Version_Available</strong> function indicates whether a specified version of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) is supported by a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Is_Version_Available_Ex</strong>](cm-is-version-available-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Is_Version_Available_Ex</strong> function indicates whether a specified version of the Plug and Play (PNP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) is supported by a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Locate_DevNode</strong>](cm-locate-devnode.md)<br/></td>
<td>The <strong>CM_Locate_DevNode</strong> function obtains a device instance handle to the device node that is associated with a specified [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Locate_DevNode_Ex</strong>](cm-locate-devnode-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Locate_DevNode</strong>](cm-locate-devnode.md) instead.
</blockquote>
<br/> The <strong>CM_Locate_DevNode_Ex</strong> function obtains a device instance handle to the device node that is associated with a specified [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327), on a local machine or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_MapCrToWin32Err</strong>](https://msdn.microsoft.com/library/windows/hardware/dn313265)<br/></td>
<td>Converts a specified <strong>CONFIGRET</strong> code to its equivalent system error code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Modify_Res_Des</strong>](cm-modify-res-des.md)<br/></td>
<td>The <strong>CM_Modify_Res_Des</strong> function modifies a specified resource descriptor on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Modify_Res_Des_Ex</strong>](cm-modify-res-des-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Modify_Res_Des</strong>](cm-modify-res-des.md) instead.
</blockquote>
<br/> The <strong>CM_Modify_Res_Des_Ex</strong> function modifies a specified resource descriptor on a local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_NOTIFY_ACTION</strong>](cm-notify-action.md)<br/></td>
<td>This enumeration identifies Plug and Play device event types.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_NOTIFY_EVENT_DATA</strong>](cm-notify-event-data.md)<br/></td>
<td>This is a device notification event data structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_NOTIFY_FILTER</strong>](cm-notify-filter.md)<br/></td>
<td>Device notification filter structure<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_Class_Key</strong>](cm-open-class-key.md)<br/></td>
<td>The <strong>CM_Open_Class_Key</strong> function opens the device setup class registry key, the device interface class registry key, or a specific subkey of a class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Open_Device_Interface_Key</strong>](cm-open-device-interface-key.md)<br/></td>
<td>The <strong>CM_Open_Device_Interface_Key</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_Device_Interface_Key_ExA</strong>](cm-open-device-interface-key-exa.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Open_Device_Interface_Key</strong>](cm-open-device-interface-key.md) instead.
</blockquote>
<br/> The <strong>CM_Open_Device_Interface_Key_ExA</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Open_Device_Interface_Key_ExW</strong>](cm-open-device-interface-key-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Open_Device_Interface_Key</strong>](cm-open-device-interface-key.md) instead.
</blockquote>
<br/> The <strong>CM_Open_Device_Interface_Key_ExW</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_DevNode_Key</strong>](cm-open-devnode-key.md)<br/></td>
<td>The <strong>CM_Open_DevNode_Key</strong> function opens a registry key for device-specific configuration information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Query_And_Remove_SubTree</strong>](cm-query-and-remove-subtree.md)<br/></td>
<td>The <strong>CM_Query_And_Remove_SubTree</strong> function checks whether a device instance and its children can be removed and, if so, it removes them.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Query_And_Remove_SubTree_Ex</strong>](cm-query-and-remove-subtree-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Query_And_Remove_SubTree</strong>](cm-query-and-remove-subtree.md) instead.
</blockquote>
<br/> The <strong>CM_Query_And_Remove_SubTree_Ex</strong> function checks whether a device instance and its children can be removed and, if so, it removes them.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Query_Resource_Conflict_List</strong>](cm-query-resource-conflict-list.md)<br/></td>
<td>The <strong>CM_Query_Resource_Conflict_List</strong> function identifies device instances having resource requirements that conflict with a specified device instance's resource description.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Reenumerate_DevNode</strong>](cm-reenumerate-devnode.md)<br/></td>
<td>The <strong>CM_Reenumerate_DevNode</strong> function enumerates the devices identified by a specified device node and all of its children.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Reenumerate_DevNode_Ex</strong>](cm-reenumerate-devnode-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Reenumerate_DevNode</strong>](cm-reenumerate-devnode.md) instead.
</blockquote>
<br/> The <strong>CM_Reenumerate_DevNode_Ex</strong> function enumerates the devices identified by a specified device node and all of its children.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Register_Notification</strong>](cm-register-notification.md)<br/></td>
<td>Use [<strong>RegisterDeviceNotification</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363431) instead of [<strong>CM_Register_Notification</strong>](cm-register-notification.md) if your code targets Windows 7 or earlier versions of Windows. Kernel mode callers should use [<strong>IoRegisterPlugPlayNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549526) instead.<br/> The [<strong>CM_Register_Notification</strong>](cm-register-notification.md) function registers an application callback routine to be called when a PnP event of the specified type occurs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Request_Device_Eject</strong>](cm-request-device-eject.md)<br/></td>
<td>The <strong>CM_Request_Device_Eject</strong> function prepares a local device instance for safe removal, if the device is removable. If the device can be physically ejected, it will be.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Request_Device_Eject_Ex</strong>](cm-request-device-eject-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Request_Device_Eject</strong>](cm-request-device-eject.md) instead.
</blockquote>
<br/> The <strong>CM_Request_Device_Eject_Ex</strong> function prepares a local or a remote device instance for safe removal, if the device is removable. If the device can be physically ejected, it will be.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Request_Eject_PC</strong>](cm-request-eject-pc.md)<br/></td>
<td>The <strong>CM_Request_Eject_PC</strong> function requests that a portable PC, which is inserted in a local [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station), be ejected.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Request_Eject_PC_Ex</strong>](cm-request-eject-pc-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Request_Eject_PC</strong>](cm-request-eject-pc.md) instead.
</blockquote>
<br/> The <strong>CM_Request_Eject_PC_Ex</strong> function requests that a portable PC, which is inserted in a local or a remote [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station), be ejected.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Class_Property</strong>](cm-set-class-property.md)<br/></td>
<td>The <strong>CM_Set_Class_Property</strong> function sets a class property for a device setup class or a device interface class.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_Class_Property_ExW</strong>](cm-set-class-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_Class_Property</strong>](cm-set-class-property.md) instead.
</blockquote>
<br/> The <strong>CM_Set_Class_Property_ExW</strong> function sets a class property for a device setup class or a device interface class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Class_Registry_Property</strong>](cm-set-class-registry-property.md)<br/></td>
<td>The <strong>CM_Set_Class_Registry_Property</strong> function sets or deletes a property of a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_Device_Interface_Property</strong>](cm-set-device-interface-property.md)<br/></td>
<td>The <strong>CM_Set_Device_Interface_Property</strong> function sets a device property of a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Device_Interface_Property_ExW</strong>](cm-set-device-interface-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_Device_Interface_Property</strong>](cm-set-device-interface-property.md) instead.
</blockquote>
<br/> The <strong>CM_Set_Device_Interface_Property_ExW</strong> function sets a device property of a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Problem</strong>](cm-set-devnode-problem.md)<br/></td>
<td>The <strong>CM_Set_DevNode_Problem</strong> function sets a problem code for a device that is installed in a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_DevNode_Problem_Ex</strong>](cm-set-devnode-problem-ex.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_DevNode_Problem</strong>](cm-set-devnode-problem.md) instead.
</blockquote>
<br/> The <strong>CM_Set_DevNode_Problem_Ex</strong> function sets a problem code for a device that is installed in a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Property</strong>](cm-set-devnode-property.md)<br/></td>
<td>The <strong>CM_Set_DevNode_Property</strong> function sets a device instance property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_DevNode_Property_ExW</strong>](cm-set-devnode-property-exw.md)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_DevNode_Property</strong>](cm-set-devnode-property.md) instead.
</blockquote>
<br/> The <strong>CM_Set_DevNode_Property_ExW</strong> function sets a device instance property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Registry_Property</strong>](cm-set-devnode-registry-property.md)<br/></td>
<td>The <strong>CM_Set_DevNode_Registry_Property</strong> function sets a specified device property in the registry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Setup_DevNode</strong>](cm-setup-devnode.md)<br/></td>
<td>The <strong>CM_Setup_DevNode</strong> function restarts a device instance that is not running because there is a problem with the device configuration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Uninstall_DevNode</strong>](cm-uninstall-devnode.md)<br/></td>
<td>The <strong>CM_Uninstall_DevNode</strong> function removes all persistent state associated with a device instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Unregister_Notification</strong>](cm-unregister-notification.md)<br/></td>
<td>Use [<strong>UnregisterDeviceNotification</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363475) instead of <strong>CM_Unregister_Notification</strong> if your code targets Windows 7 or earlier versions of Windows.<br/> The <strong>CM_Unregister_Notification</strong> function closes the specified HCMNOTIFICATION handle.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CMP_WaitNoPendingInstallEvents</strong>](cmp-waitnopendinginstallevents.md)<br/></td>
<td>The <strong>CMP_WaitNoPendingInstallEvents</strong> function waits until there are no pending device installation activities for the PnP manager to perform.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CONFLICT_DETAILS</strong>](conflict-details.md)<br/></td>
<td>The CONFLICT_DETAILS structure is used as a parameter to the [<strong>CM_Get_Resource_Conflict_Details</strong>](cm-get-resource-conflict-details.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CS_DES</strong>](cs-des.md)<br/></td>
<td>The CS_DES structure is used for specifying a resource list that describes device class-specific resource usage for a device instance. For more information about resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CS_RESOURCE</strong>](cs-resource.md)<br/></td>
<td>The CS_RESOURCE structure is used for specifying a resource list that describes device class-specific resource usage for a device instance. For more information about resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DMA_DES</strong>](dma-des.md)<br/></td>
<td>The DMA_DES structure is used for specifying either a resource list or a resource requirements list that describes direct memory access (DMA) channel usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DMA_RANGE</strong>](dma-range.md)<br/></td>
<td>The DMA_RANGE structure specifies a resource requirements list that describes DMA channel usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DMA_RESOURCE</strong>](dma-resource.md)<br/></td>
<td>The DMA_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes DMA channel usage for a device instance. For more information about resource list and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IO_DES</strong>](io-des.md)<br/></td>
<td>The IO_DES structure is used for specifying either a resource list or a resource requirements list that describes I/O port usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IO_RANGE</strong>](io-range.md)<br/></td>
<td>The IO_RANGE structure specifies a resource requirements list that describes I/O port usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IO_RESOURCE</strong>](io-resource.md)<br/></td>
<td>The IO_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes I/O port usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRQ_DES</strong>](irq-des.md)<br/></td>
<td>The IRQ_DES structure is used for specifying either a resource list or a resource requirements list that describes IRQ line usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRQ_RANGE</strong>](irq-range.md)<br/></td>
<td>The IRQ_RANGE structure specifies a resource requirements list that describes IRQ line usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRQ_RESOURCE</strong>](irq-resource.md)<br/></td>
<td>The IRQ_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes IRQ line usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MEM_DES</strong>](mem-des.md)<br/></td>
<td>The MEM_DES structure is used for specifying either a resource list or a resource requirements list that describes memory usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MEM_RANGE</strong>](mem-range.md)<br/></td>
<td>The MEM_RANGE structure specifies a resource requirements list that describes memory usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MEM_RESOURCE</strong>](mem-resource.md)<br/></td>
<td>The MEM_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes memory usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MFCARD_DES</strong>](mfcard-des.md)<br/></td>
<td>The MFCARD_DES structure is used for specifying either a resource list or a resource requirements list that describes resource usage by <em>one</em> of the hardware functions provided by an instance of a multifunction device. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MFCARD_RESOURCE</strong>](mfcard-resource.md)<br/></td>
<td>The MFCARD_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes resource usage by <em>one</em> of the hardware functions provided by an instance of a multifunction device. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PCCARD_DES</strong>](pccard-des.md)<br/></td>
<td>The PCCARD_DES structure is used for specifying either a resource list or a resource requirements list that describes resource usage by a PC Card instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>PCCARD_RESOURCE</strong>](pccard-resource.md)<br/></td>
<td>The PCCARD_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes resource usage by a PC Card instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Cfgmgr32.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






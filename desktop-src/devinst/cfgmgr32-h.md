---
title: Cfgmgr32.h
description: This section contains reference topics for the Cfgmgr32.h header.
ms.assetid: 73b4b2ec-ce3d-47c1-9b0e-1052f390ae94
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>BUSNUMBER_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-busnumber_des_s)<br/></td>
<td>The BUSNUMBER_DES structure is used for specifying either a resource list or a resource requirements list that describes bus number usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>BUSNUMBER_RANGE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-busnumber_range_s)<br/></td>
<td>The BUSNUMBER_RANGE structure specifies a resource requirements list that describes bus number usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BUSNUMBER_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-busnumber_resource_s)<br/></td>
<td>The BUSNUMBER_RESOURCE structure specifies either a resource list or a resource requirements list that describes bus number usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_Empty_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_empty_log_conf)<br/></td>
<td>The <strong>CM_Add_Empty_Log_Conf</strong> function creates an empty [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), for a specified configuration type and a specified device instance, on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_Empty_Log_Conf_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_empty_log_conf_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_Empty_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_empty_log_conf) instead.
</blockquote>
<br/> The <strong>CM_Add_Empty_Log_Conf_Ex</strong> function creates an empty [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), for a specified configuration type and a specified device instance, on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_ID</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_idw)<br/></td>
<td>The <strong>CM_Add_ID</strong> function appends a specified [device ID](https://msdn.microsoft.com/library/windows/hardware/ff541237) (if not already present) to a [device instance's](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) [hardware ID](https://msdn.microsoft.com/library/windows/hardware/ff546152) list or [compatible ID](https://msdn.microsoft.com/library/windows/hardware/ff539950) list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_ID_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_id_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_ID</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_idw) instead.
</blockquote>
<br/> The <strong>CM_Add_ID_Ex</strong> function appends a [device ID](https://msdn.microsoft.com/library/windows/hardware/ff541237) (if not already present) to a device instance's [hardware ID](https://msdn.microsoft.com/library/windows/hardware/ff546152) list or [compatible ID](https://msdn.microsoft.com/library/windows/hardware/ff539950) list, on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Add_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_res_des)<br/></td>
<td>The <strong>CM_Add_Res_Des</strong> function adds a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) to a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Add_Res_Des_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_res_des_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Add_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_add_res_des) instead.
</blockquote>
<br/> The <strong>CM_Add_Res_Des_Ex</strong> function adds a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) to a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg). The logical configuration can be on either the local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Connect_Machine</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_connect_machinew)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning in Windows 8 and Windows Server 2012 functionality to access remote machines has been removed. You cannot access remote machines when running on these versions of Windows.
</blockquote>
<br/> The <strong>CM_Connect_Machine</strong> function creates a connection to a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_Class_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_class_key)<br/></td>
<td>The <strong>CM_Delete_Class_Key</strong> function removes the specified installed [device class](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class) from the system.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Delete_Device_Interface_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_device_interface_keyw)<br/></td>
<td>The <strong>CM_Delete_Device_Interface_Key</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_Device_Interface_Key_ExA</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_device_interface_key_exa)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Delete_Device_Interface_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_device_interface_keyw) instead.
</blockquote>
<br/> The <strong>CM_Delete_Device_Interface_Key_ExA</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Delete_Device_Interface_Key_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_device_interface_key_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Delete_Device_Interface_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_device_interface_keyw) instead.
</blockquote>
<br/> The <strong>CM_Delete_Device_Interface_Key_ExW</strong> function deletes the registry subkey that is used by applications and drivers to store interface-specific information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Delete_DevNode_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_delete_devnode_key)<br/></td>
<td>The <strong>CM_Delete_DevNode_Key</strong> function deletes the specified user-accessible registry keys that are associated with a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Disable_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_disable_devnode)<br/></td>
<td>The <strong>CM_Disable_DevNode</strong> function disables a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Disconnect_Machine</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_disconnect_machine)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning in Windows 8 and Windows Server 2012 functionality to access remote machines has been removed. You cannot access remote machines when running on these versions of Windows.
</blockquote>
<br/> The <strong>CM_Disconnect_Machine</strong> function removes a connection to a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enable_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enable_devnode)<br/></td>
<td>The <strong>CM_Enable_DevNode</strong> function enables a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Enumerate_Classes</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_classes)<br/></td>
<td>The <strong>CM_Enumerate_Classes</strong> function, when called repeatedly, enumerates the local machine's installed [device classes](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class) by supplying each class's GUID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enumerate_Classes_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_classes_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Enumerate_Classes</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_classes) instead.
</blockquote>
<br/> The <strong>CM_Enumerate_Classes_Ex</strong> function, when called repeatedly, enumerates a local or a remote machine's installed [device classes](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-class), by supplying each class's GUID.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Enumerate_Enumerators</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_enumeratorsw)<br/></td>
<td>The <strong>CM_Enumerate_Enumerators</strong> function enumerates the local machine's device enumerators by supplying each enumerator's name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Enumerate_Enumerators_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_enumerators_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Enumerate_Enumerators</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_enumerate_enumeratorsw) instead.
</blockquote>
<br/> The <strong>CM_Enumerate_Enumerators_Ex</strong> function enumerates a local or a remote machine's device enumerators, by supplying each enumerator's name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_log_conf)<br/></td>
<td>The <strong>CM_Free_Log_Conf</strong> function removes a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) and all associated [resource descriptors](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Log_Conf_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_log_conf_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Free_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_log_conf) instead.
</blockquote>
<br/> The <strong>CM_Free_Log_Conf_Ex</strong> function removes a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) and all associated [resource descriptors](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from either a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Log_Conf_Handle</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_log_conf_handle)<br/></td>
<td>The <strong>CM_Free_Log_Conf_Handle</strong> function invalidates a logical configuration handle and frees its associated memory allocation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_res_des)<br/></td>
<td>The <strong>CM_Free_Res_Des</strong> function removes a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Res_Des_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_res_des_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Free_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_res_des) instead.
</blockquote>
<br/> The <strong>CM_Free_Res_Des_Ex</strong> function removes a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) from a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on either a local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Free_Res_Des_Handle</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_res_des_handle)<br/></td>
<td>The <strong>CM_Free_Res_Des_Handle</strong> function invalidates a resource description handle and frees its associated memory allocation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Free_Resource_Conflict_Handle</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_free_resource_conflict_handle)<br/></td>
<td>The <strong>CM_Free_Resource_Conflict_Handle</strong> function invalidates a handle to a resource conflict list, and frees the handle's associated memory allocation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Child</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_child)<br/></td>
<td>The <strong>CM_Get_Child</strong> function is used to retrieve a device instance handle to the first child node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Child_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_child_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Child</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_child) instead.
</blockquote>
<br/> The <strong>CM_Get_Child_Ex</strong> function is used to retrieve a device instance handle to the first child node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw)<br/></td>
<td>The <strong>CM_Get_Class_Property</strong> function retrieves a device property that is set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Class_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Class_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Get_Class_Property_ExW</strong> function retrieves a device property that is set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_property_keys)<br/></td>
<td>The <strong>CM_Get_Class_Property_Keys</strong> function retrieves an array of the device property keys that represent the device properties that are set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Class_Property_Keys_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_property_keys_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Class_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_property_keys) instead.
</blockquote>
<br/> The <strong>CM_Get_Class_Property_Keys_Ex</strong> function retrieves an array of the device property keys that represent the device properties that are set for a [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) or [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Class_Registry_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_class_registry_propertyw)<br/></td>
<td>The <strong>CM_Get_Class_Registry_Property</strong> function retrieves a [device setup class property](https://msdn.microsoft.com/library/windows/hardware/ff537744).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Depth</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_depth)<br/></td>
<td>The <strong>CM_Get_Depth</strong> function is used to obtain the depth of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) within the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Depth_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_depth_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Depth</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_depth) instead.
</blockquote>
<br/> The <strong>CM_Get_Depth_Ex</strong> function is used to obtain the depth of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) within a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_idw)<br/></td>
<td>The <strong>CM_Get_Device_ID</strong> function retrieves the [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_idw) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_Ex</strong> function retrieves the [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_List</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista)<br/></td>
<td>The <strong>CM_Get_Device_ID_List</strong> function retrieves a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the local computer's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_List_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_List</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_List_Ex</strong> function retrieves a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_List_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea)<br/></td>
<td>The <strong>CM_Get_Device_ID_List_Size</strong> function retrieves the buffer size required to hold a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for the local machine's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_List_Size_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_size_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_List_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_List_Size_Ex</strong> function retrieves the buffer size required to hold a list of [device instance IDs](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a local or a remote machine's [device instances](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_ID_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_size)<br/></td>
<td>The <strong>CM_Get_Device_ID_Size</strong> function retrieves the buffer size required to hold a [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_ID_Size_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_size_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_ID_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_id_size) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_ID_Size_Ex</strong> function retrieves the buffer size required to hold a [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Alias</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_aliasw)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Alias</strong> function returns the alias of the specified device interface instance, if the alias exists.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_List</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista)<br/></td>
<td>The <strong>CM_Get_Device_Interface_List</strong> function retrieves a list of device interface instances that belong to a specified [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_List_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizea)<br/></td>
<td>The <strong>CM_Get_Device_Interface_List_Size</strong> function retrieves the buffer size that must be passed to the [<strong>CM_Get_Device_Interface_List</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Property</strong> function retrieves a device property that is set for a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_Interface_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_Interface_Property_ExW</strong> function retrieves a device property that is set for a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Device_Interface_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_keysw)<br/></td>
<td>The <strong>CM_Get_Device_Interface_Property_Keys</strong> function retrieves an array of device property keys that represent the device properties that are set for a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Device_Interface_Property_Keys_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_keys_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Device_Interface_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_keysw) instead.
</blockquote>
<br/> The <strong>CM_Get_Device_Interface_Property_Keys_ExW</strong> function retrieves an array of device property keys that represent the device properties that are set for a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw)<br/></td>
<td>The <strong>CM_Get_DevNode_Property</strong> function retrieves a device instance property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Property_ExW</strong> function retrieves a device instance property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_keys)<br/></td>
<td>The <strong>CM_Get_DevNode_Property_Keys</strong> function retrieves an array of the device property keys that represent the device properties that are set for a device instance.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Property_Keys_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_keys_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Property_Keys</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_keys) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Property_Keys_Ex</strong> function retrieves an array of the device property keys that represent the device properties that are set for a device instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Registry_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_registry_propertyw)<br/></td>
<td>The <strong>CM_Get_DevNode_Registry_Property</strong> function retrieves a specified device property from the registry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_DevNode_Status</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_status)<br/></td>
<td>The <strong>CM_Get_DevNode_Status</strong> function obtains the status of a device instance from its device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_DevNode_Status_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_status_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_DevNode_Status</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_devnode_status) instead.
</blockquote>
<br/> The <strong>CM_Get_DevNode_Status_Ex</strong> function obtains the status of a device instance from its device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) on a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_First_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_first_log_conf)<br/></td>
<td>The <strong>CM_Get_First_Log_Conf</strong> function obtains the first [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg), of a specified configuration type, associated with a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_First_Log_Conf_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_first_log_conf_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_First_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_first_log_conf) instead.
</blockquote>
<br/> The <strong>CM_Get_First_Log_Conf_Ex</strong> function obtains the first [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specified [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_HW_Prof_Flags</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_hw_prof_flagsa)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_HW_Prof_Flags</strong> function retrieves the [hardware profile](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-profile)-specific configuration flags for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_HW_Prof_Flags_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_hw_prof_flags_exa)<br/></td>
<td><blockquote>
[!Note]<br />
This function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_HW_Prof_Flags_Ex</strong> function retrieves the [hardware profile](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-profile)-specific configuration flags for a [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a remote machine or a local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Log_Conf_Priority</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_log_conf_priority)<br/></td>
<td>The <strong>CM_Get_Log_Conf_Priority</strong> function obtains the configuration priority of a specified [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Log_Conf_Priority_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_log_conf_priority_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Log_Conf_Priority</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_log_conf_priority) instead.
</blockquote>
<br/> The <strong>CM_Get_Log_Conf_Priority_Ex</strong> function obtains the configuration priority of a specified [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Next_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_log_conf)<br/></td>
<td>The <strong>CM_Get_Next_Log_Conf</strong> function obtains the next [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specific [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Next_Log_Conf_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_log_conf_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Next_Log_Conf</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_log_conf) instead.
</blockquote>
<br/> The <strong>CM_Get_Next_Log_Conf_Ex</strong> function obtains the next [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) associated with a specific [device instance](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Next_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_res_des)<br/></td>
<td>The <strong>CM_Get_Next_Res_Des</strong> function obtains a handle to the next [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor), of a specified resource type, for a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Next_Res_Des_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_res_des_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Next_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_next_res_des) instead.
</blockquote>
<br/> The <strong>CM_Get_Next_Res_Des_Ex</strong> function obtains a handle to the next [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor), of a specified resource type, for a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Parent</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_parent)<br/></td>
<td>The <strong>CM_Get_Parent</strong> function obtains a device instance handle to the parent node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's device tree.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Parent_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_parent_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Parent</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_parent) instead.
</blockquote>
<br/> The <strong>CM_Get_Parent_Ex</strong> function obtains a device instance handle to the parent node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Res_Des_Data</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data)<br/></td>
<td>The <strong>CM_Get_Res_Des_Data</strong> function retrieves the information stored in a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Res_Des_Data_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Res_Des_Data</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data) instead.
</blockquote>
<br/> The <strong>CM_Get_Res_Des_Data_Ex</strong> function retrieves the information stored in a [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Res_Des_Data_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data_size)<br/></td>
<td>The <strong>CM_Get_Res_Des_Data_Size</strong> function obtains the buffer size required to hold the information contained in a specified [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Res_Des_Data_Size_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data_size_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Res_Des_Data_Size</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_res_des_data_size) instead.
</blockquote>
<br/> The <strong>CM_Get_Res_Des_Data_Size_Ex</strong> function obtains the buffer size required to hold the information contained in a specified [resource descriptor](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-resource-descriptor) on a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Resource_Conflict_Count</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_resource_conflict_count)<br/></td>
<td>The <strong>CM_Get_Resource_Conflict_Count</strong> function obtains the number of conflicts contained in a specified resource conflict list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Resource_Conflict_Details</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_resource_conflict_detailsw)<br/></td>
<td>The <strong>CM_Get_Resource_Conflict_Details</strong> function obtains the details about one of the resource conflicts in a conflict list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Sibling</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_sibling)<br/></td>
<td>The <strong>CM_Get_Sibling</strong> function obtains a device instance handle to the next sibling node of a specified device node ([devnode](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the local machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Sibling_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_sibling_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Get_Sibling</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_sibling) instead.
</blockquote>
<br/> The <strong>CM_Get_Sibling_Ex</strong> function obtains a device instance handle to the next sibling node of a specified device node, in a local or a remote machine's [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Get_Version</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_version)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_Version</strong> function returns version 4.0 of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) for a local machine. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Get_Version_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_version_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Get_Version_Ex</strong> function returns version 4.0 of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) for a local or a remote machine. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Is_Dock_Station_Present</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_is_dock_station_present)<br/></td>
<td>The <strong>CM_Is_Dock_Station_Present</strong> function identifies whether a [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station) is present in a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Is_Dock_Station_Present_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_is_dock_station_present_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Is_Dock_Station_Present</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_is_dock_station_present) instead.
</blockquote>
<br/> The <strong>CM_Is_Dock_Station_Present_Ex</strong> function identifies whether a [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station) is present in a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Is_Version_Available</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_is_version_available)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Is_Version_Available</strong> function indicates whether a specified version of the Plug and Play (PnP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) is supported by a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Is_Version_Available_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_is_version_available_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated and should not be used.
</blockquote>
<br/> The <strong>CM_Is_Version_Available_Ex</strong> function indicates whether a specified version of the Plug and Play (PNP) Configuration Manager [DLL](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll) (<em>Cfgmgr32.dll</em>) is supported by a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Locate_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_locate_devnodea)<br/></td>
<td>The <strong>CM_Locate_DevNode</strong> function obtains a device instance handle to the device node that is associated with a specified [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327) on the local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Locate_DevNode_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_locate_devnode_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Locate_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_locate_devnodea) instead.
</blockquote>
<br/> The <strong>CM_Locate_DevNode_Ex</strong> function obtains a device instance handle to the device node that is associated with a specified [device instance ID](https://msdn.microsoft.com/library/windows/hardware/ff541327), on a local machine or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_MapCrToWin32Err</strong>](https://msdn.microsoft.com/library/windows/hardware/dn313265)<br/></td>
<td>Converts a specified <strong>CONFIGRET</strong> code to its equivalent system error code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Modify_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_modify_res_des)<br/></td>
<td>The <strong>CM_Modify_Res_Des</strong> function modifies a specified resource descriptor on the local machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Modify_Res_Des_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_modify_res_des_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Modify_Res_Des</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_modify_res_des) instead.
</blockquote>
<br/> The <strong>CM_Modify_Res_Des_Ex</strong> function modifies a specified resource descriptor on a local or a remote machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_NOTIFY_ACTION</strong>](/windows/desktop/api/Cfgmgr32/ne-cfgmgr32-_cm_notify_action)<br/></td>
<td>This enumeration identifies Plug and Play device event types.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_NOTIFY_EVENT_DATA</strong>](/windows/desktop/api/Cfgmgr32/ns-cfgmgr32-_cm_notify_event_data)<br/></td>
<td>This is a device notification event data structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_NOTIFY_FILTER</strong>](/windows/desktop/api/Cfgmgr32/ns-cfgmgr32-_cm_notify_filter)<br/></td>
<td>Device notification filter structure<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_Class_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_open_class_keyw)<br/></td>
<td>The <strong>CM_Open_Class_Key</strong> function opens the device setup class registry key, the device interface class registry key, or a specific subkey of a class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Open_Device_Interface_Key</strong>](https://www.bing.com/search?q=<strong>CM_Open_Device_Interface_Key</strong>)<br/></td>
<td>The <strong>CM_Open_Device_Interface_Key</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_Device_Interface_Key_ExA</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keya)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Open_Device_Interface_Key</strong>](https://www.bing.com/search?q=<strong>CM_Open_Device_Interface_Key</strong>) instead.
</blockquote>
<br/> The <strong>CM_Open_Device_Interface_Key_ExA</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Open_Device_Interface_Key_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_open_device_interface_key_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Open_Device_Interface_Key</strong>](https://www.bing.com/search?q=<strong>CM_Open_Device_Interface_Key</strong>) instead.
</blockquote>
<br/> The <strong>CM_Open_Device_Interface_Key_ExW</strong> function opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Open_DevNode_Key</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_open_devnode_key)<br/></td>
<td>The <strong>CM_Open_DevNode_Key</strong> function opens a registry key for device-specific configuration information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Query_And_Remove_SubTree</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_query_and_remove_subtreew)<br/></td>
<td>The <strong>CM_Query_And_Remove_SubTree</strong> function checks whether a device instance and its children can be removed and, if so, it removes them.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Query_And_Remove_SubTree_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_query_and_remove_subtree_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Query_And_Remove_SubTree</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_query_and_remove_subtreew) instead.
</blockquote>
<br/> The <strong>CM_Query_And_Remove_SubTree_Ex</strong> function checks whether a device instance and its children can be removed and, if so, it removes them.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Query_Resource_Conflict_List</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_query_resource_conflict_list)<br/></td>
<td>The <strong>CM_Query_Resource_Conflict_List</strong> function identifies device instances having resource requirements that conflict with a specified device instance's resource description.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Reenumerate_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_reenumerate_devnode)<br/></td>
<td>The <strong>CM_Reenumerate_DevNode</strong> function enumerates the devices identified by a specified device node and all of its children.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Reenumerate_DevNode_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_reenumerate_devnode_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Reenumerate_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_reenumerate_devnode) instead.
</blockquote>
<br/> The <strong>CM_Reenumerate_DevNode_Ex</strong> function enumerates the devices identified by a specified device node and all of its children.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Register_Notification</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_register_notification)<br/></td>
<td>Use [<strong>RegisterDeviceNotification</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363431) instead of [<strong>CM_Register_Notification</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_register_notification) if your code targets Windows 7 or earlier versions of Windows. Kernel mode callers should use [<strong>IoRegisterPlugPlayNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549526) instead.<br/> The [<strong>CM_Register_Notification</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_register_notification) function registers an application callback routine to be called when a PnP event of the specified type occurs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Request_Device_Eject</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_device_ejectw)<br/></td>
<td>The <strong>CM_Request_Device_Eject</strong> function prepares a local device instance for safe removal, if the device is removable. If the device can be physically ejected, it will be.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Request_Device_Eject_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_device_eject_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Request_Device_Eject</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_device_ejectw) instead.
</blockquote>
<br/> The <strong>CM_Request_Device_Eject_Ex</strong> function prepares a local or a remote device instance for safe removal, if the device is removable. If the device can be physically ejected, it will be.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Request_Eject_PC</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_eject_pc)<br/></td>
<td>The <strong>CM_Request_Eject_PC</strong> function requests that a portable PC, which is inserted in a local [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station), be ejected.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Request_Eject_PC_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_eject_pc_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Request_Eject_PC</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_request_eject_pc) instead.
</blockquote>
<br/> The <strong>CM_Request_Eject_PC_Ex</strong> function requests that a portable PC, which is inserted in a local or a remote [docking station](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-docking-station), be ejected.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Class_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw)<br/></td>
<td>The <strong>CM_Set_Class_Property</strong> function sets a class property for a device setup class or a device interface class.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_Class_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_class_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_Class_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Set_Class_Property_ExW</strong> function sets a class property for a device setup class or a device interface class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Class_Registry_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_class_registry_propertyw)<br/></td>
<td>The <strong>CM_Set_Class_Registry_Property</strong> function sets or deletes a property of a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_Device_Interface_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw)<br/></td>
<td>The <strong>CM_Set_Device_Interface_Property</strong> function sets a device property of a device interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_Device_Interface_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_device_interface_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_Device_Interface_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Set_Device_Interface_Property_ExW</strong> function sets a device property of a device interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Problem</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_problem)<br/></td>
<td>The <strong>CM_Set_DevNode_Problem</strong> function sets a problem code for a device that is installed in a local machine.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_DevNode_Problem_Ex</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_problem_ex)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_DevNode_Problem</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_problem) instead.
</blockquote>
<br/> The <strong>CM_Set_DevNode_Problem_Ex</strong> function sets a problem code for a device that is installed in a local or a remote machine.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw)<br/></td>
<td>The <strong>CM_Set_DevNode_Property</strong> function sets a device instance property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Set_DevNode_Property_ExW</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_property_exw)<br/></td>
<td><blockquote>
[!Note]<br />
Beginning with Windows 8 and Windows Server 2012, this function has been deprecated. Please use [<strong>CM_Set_DevNode_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw) instead.
</blockquote>
<br/> The <strong>CM_Set_DevNode_Property_ExW</strong> function sets a device instance property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Set_DevNode_Registry_Property</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_set_devnode_registry_propertyw)<br/></td>
<td>The <strong>CM_Set_DevNode_Registry_Property</strong> function sets a specified device property in the registry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Setup_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_setup_devnode)<br/></td>
<td>The <strong>CM_Setup_DevNode</strong> function restarts a device instance that is not running because there is a problem with the device configuration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_Uninstall_DevNode</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_uninstall_devnode)<br/></td>
<td>The <strong>CM_Uninstall_DevNode</strong> function removes all persistent state associated with a device instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_Unregister_Notification</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_unregister_notification)<br/></td>
<td>Use [<strong>UnregisterDeviceNotification</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363475) instead of <strong>CM_Unregister_Notification</strong> if your code targets Windows 7 or earlier versions of Windows.<br/> The <strong>CM_Unregister_Notification</strong> function closes the specified HCMNOTIFICATION handle.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CMP_WaitNoPendingInstallEvents</strong>](https://msdn.microsoft.com/en-us/library/Ff537916(v=VS.85).aspx)<br/></td>
<td>The <strong>CMP_WaitNoPendingInstallEvents</strong> function waits until there are no pending device installation activities for the PnP manager to perform.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CONFLICT_DETAILS</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-_conflict_details_a)<br/></td>
<td>The CONFLICT_DETAILS structure is used as a parameter to the [<strong>CM_Get_Resource_Conflict_Details</strong>](/windows/desktop/api/Cfgmgr32/nf-cfgmgr32-cm_get_resource_conflict_detailsw) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CS_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-cs_des_s)<br/></td>
<td>The CS_DES structure is used for specifying a resource list that describes device class-specific resource usage for a device instance. For more information about resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CS_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-cs_resource_s)<br/></td>
<td>The CS_RESOURCE structure is used for specifying a resource list that describes device class-specific resource usage for a device instance. For more information about resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DMA_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-dma_des_s)<br/></td>
<td>The DMA_DES structure is used for specifying either a resource list or a resource requirements list that describes direct memory access (DMA) channel usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DMA_RANGE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-dma_range_s)<br/></td>
<td>The DMA_RANGE structure specifies a resource requirements list that describes DMA channel usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DMA_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-dma_resource_s)<br/></td>
<td>The DMA_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes DMA channel usage for a device instance. For more information about resource list and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IO_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-io_des_s)<br/></td>
<td>The IO_DES structure is used for specifying either a resource list or a resource requirements list that describes I/O port usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IO_RANGE</strong>](/windows/desktop/api/Cfgmgr32/ns-cfgmgr32-io_range_s)<br/></td>
<td>The IO_RANGE structure specifies a resource requirements list that describes I/O port usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IO_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-io_resource_s)<br/></td>
<td>The IO_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes I/O port usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRQ_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-irq_des_32_s)<br/></td>
<td>The IRQ_DES structure is used for specifying either a resource list or a resource requirements list that describes IRQ line usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRQ_RANGE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-irq_range_s)<br/></td>
<td>The IRQ_RANGE structure specifies a resource requirements list that describes IRQ line usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRQ_RESOURCE</strong>](/windows/desktop/api/Cfgmgr32/ns-cfgmgr32-irq_resource_32_s)<br/></td>
<td>The IRQ_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes IRQ line usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MEM_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-mem_des_s)<br/></td>
<td>The MEM_DES structure is used for specifying either a resource list or a resource requirements list that describes memory usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MEM_RANGE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-mem_range_s)<br/></td>
<td>The MEM_RANGE structure specifies a resource requirements list that describes memory usage for a device instance. For more information about resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MEM_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-mem_resource_s)<br/></td>
<td>The MEM_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes memory usage for a device instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MFCARD_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-mfcard_des_s)<br/></td>
<td>The MFCARD_DES structure is used for specifying either a resource list or a resource requirements list that describes resource usage by <em>one</em> of the hardware functions provided by an instance of a multifunction device. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MFCARD_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-mfcard_resource_s)<br/></td>
<td>The MFCARD_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes resource usage by <em>one</em> of the hardware functions provided by an instance of a multifunction device. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PCCARD_DES</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-pccard_des_s)<br/></td>
<td>The PCCARD_DES structure is used for specifying either a resource list or a resource requirements list that describes resource usage by a PC Card instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
<tr class="even">
<td>[<strong>PCCARD_RESOURCE</strong>](/windows/desktop/api/cfgmgr32/ns-cfgmgr32-pccard_resource_s)<br/></td>
<td>The PCCARD_RESOURCE structure is used for specifying either a resource list or a resource requirements list that describes resource usage by a PC Card instance. For more information about resource lists and resource requirements lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Cfgmgr32.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






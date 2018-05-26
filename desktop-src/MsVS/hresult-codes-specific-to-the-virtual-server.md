---
title: HRESULT Codes Specific to the Virtual Server
description: HRESULT Codes Specific to the Virtual Server
ms.assetid: 3b3e2a9a-c88b-4712-aa17-de17b0db4a5f
topic_type:
- apiref
api_name:
- VM_E_TIMED_OUT
- VM_E_OUT_OF_RESOURCE
- VM_E_TOO_MANY_VMS
- VM_E_VM_NOT_RUNNING
- VM_E_VM_UNKNOWN
- VM_E_OUT_OF_RESERVE
- VM_E_APP_SHUTTING_DOWN
- VM_E_SCRIPT_ALREADY_EXISTS
- VM_E_PREF_NOT_FOUND
- VM_E_PREF_ILLEGAL_VALUE
- VM_E_PREF_VM_ACTIVE
- VM_E_PREF_CONFIG_UPDATED_VM_ACTIVE
- VM_E_PREF_UNLOADABLE_ACTIVATION
- VM_E_PREF_SAVED_STATE_BAD_VERSION
- VM_E_PREF_SAVED_STATE_ACCESS_DENIED
- VM_E_CONFIG_NO_NAME
- VM_E_CONFIG_NAME_TOO_LONG
- VM_E_CONFIG_NAME_INVALID_CHAR
- VM_E_CONFIG_DUPLICATE_NAME
- VM_E_VM_RUNNING
- VM_E_VM_NO_SAVED_STATE
- VM_E_DRIVE_INVALID
- VM_E_DRIVE_BUS_LOC_IN_USE
- VM_E_ADDITIONS_NOT_AVAIL
- VM_E_ADDITIONS_FEATURE_NOT_AVAIL
- VM_E_FOLDER_NOT_SHARED
- VM_E_VM_PAUSED
- VM_E_MEDIA_UNMOUNT_FAIL
- VM_E_IMAGE_CAPTURE_FAIL
- VM_E_HOST_FLOPPY_CAPTURE_FAIL
- VM_E_NO_MEDIA_CAPTURED
- VM_E_PARENT_PATH_NOT_FOUND
- VM_E_FILE_TOO_LARGE_FOR_VOLUME
- VM_E_FILE_READ_ONLY
- VM_E_WRONG_HD_IMAGE_TYPE
- VM_E_HD_IMAGE_OPEN_FAIL
- VM_E_HOST_DRIVE_NOT_FOUND
- VM_E_HD_IMAGE_ACCESS
- VM_E_INVALID_HD_FILE
- VM_E_IMAGE_SIZE_TOO_LARGE
- VM_E_IMAGE_SIZE_TOO_SMALL
- VM_E_PARENT_CHILD_ID_MISMATCH
- VM_E_ADAPTER_NOT_FOUND
- VM_E_VIRTUAL_NETWORK_NAME_ALREADY_EXISTS
- VM_E_INVALID_VIRTUAL_NETWORK_ID
- VM_E_CANT_SET_ETHERNET_ADDRESS
- VM_E_INVALID_IP_ADDRESS
- VM_E_INVALID_NETWORK_ADDRESS
- VM_E_INVALID_NETWORK_MASK
- VM_E_INVALID_STARTING_ADDRESS
- VM_E_INVALID_ENDING_ADDRESS
- VM_E_INVALID_ADDRESS_RANGE
- VM_E_CANT_SET_DYNAMIC_MAC_ADDRESS
- VM_E_DRIVE_IN_USE
- VM_E_MEDIA_WRONG_TYPE
- VM_E_NO_LICENSE
- VM_E_INVALID_LICENSE
- VM_E_INVALID_LICENSE_KEY
- VM_E_INVALID_LICENSE_VALUE
- VM_E_LICENSE_ACTIVE_VM_LIMIT
- VM_E_LICENSE_HOST_MEMORY_LIMIT
- VM_E_LICENSE_VM_MEMORY_LIMIT
- VM_E_NOT_A_TRIAL_VERSION
- VM_E_NON_ACTIVE_TRIAL
- VM_E_MOUSE_NOT_ACTIVE
- VM_E_USING_ABSOLUTE_COORDINATES
- VM_E_USING_RELATIVE_COORDINATES
- VM_E_SET_EXCLUSIVE_MODE_FAIL
- VM_E_NO_DISPLAY
- VM_E_SECURITY_DUPLICATE_USER
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HRESULT Codes Specific to the Virtual Server

<dl> <dt>

<span id="VM_E_TIMED_OUT"></span><span id="vm_e_timed_out"></span>**VM\_E\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

0xA0040202
</dt> <dt>



Operation timed out.


</dt> </dl> </dd> <dt>

<span id="VM_E_OUT_OF_RESOURCE"></span><span id="vm_e_out_of_resource"></span>**VM\_E\_OUT\_OF\_RESOURCE**
</dt> <dd> <dl> <dt>

0xA0040203
</dt> <dt>



Out of resources.


</dt> </dl> </dd> <dt>

<span id="VM_E_TOO_MANY_VMS"></span><span id="vm_e_too_many_vms"></span>**VM\_E\_TOO\_MANY\_VMS**
</dt> <dd> <dl> <dt>

0xA0040204
</dt> <dt>



Too many virtual machines started.


</dt> </dl> </dd> <dt>

<span id="VM_E_VM_NOT_RUNNING"></span><span id="vm_e_vm_not_running"></span>**VM\_E\_VM\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

0xA0040206
</dt> <dt>



The virtual machine must be running for this operation.


</dt> </dl> </dd> <dt>

<span id="VM_E_VM_UNKNOWN"></span><span id="vm_e_vm_unknown"></span>**VM\_E\_VM\_UNKNOWN**
</dt> <dd> <dl> <dt>

0xA0040207
</dt> <dt>



Could not find the specified virtual machine.


</dt> </dl> </dd> <dt>

<span id="VM_E_OUT_OF_RESERVE"></span><span id="vm_e_out_of_reserve"></span>**VM\_E\_OUT\_OF\_RESERVE**
</dt> <dd> <dl> <dt>

0xA0040208
</dt> <dt>



A virtual machine could not be started because its resource allocation exceeds the amount of host resources available.


</dt> </dl> </dd> <dt>

<span id="VM_E_APP_SHUTTING_DOWN"></span><span id="vm_e_app_shutting_down"></span>**VM\_E\_APP\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

0xA0040209
</dt> <dt>



The operation could not be done because Virtual Server is shutting down. This is normally caused when a user tries to start an asynchronous operation (such as running a virtual machine or creating a virtual hard disk image) after an administrator has started the server's shutdown process.


</dt> </dl> </dd> <dt>

<span id="VM_E_SCRIPT_ALREADY_EXISTS"></span><span id="vm_e_script_already_exists"></span>**VM\_E\_SCRIPT\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

0xA004020A
</dt> <dt>



A script is already attached to this event.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_NOT_FOUND"></span><span id="vm_e_pref_not_found"></span>**VM\_E\_PREF\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0xA0040300
</dt> <dt>



Preference was not found.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_ILLEGAL_VALUE"></span><span id="vm_e_pref_illegal_value"></span>**VM\_E\_PREF\_ILLEGAL\_VALUE**
</dt> <dd> <dl> <dt>

0xA0040301
</dt> <dt>



Illegal preference value was specified.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_VM_ACTIVE"></span><span id="vm_e_pref_vm_active"></span>**VM\_E\_PREF\_VM\_ACTIVE**
</dt> <dd> <dl> <dt>

0xA0040302
</dt> <dt>



Preference cannot be changed for a running or saved virtual machine.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_CONFIG_UPDATED_VM_ACTIVE"></span><span id="vm_e_pref_config_updated_vm_active"></span>**VM\_E\_PREF\_CONFIG\_UPDATED\_VM\_ACTIVE**
</dt> <dd> <dl> <dt>

0xA0040303
</dt> <dt>



Preference change was successful but will not take effect until the next time the virtual machine is started.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_UNLOADABLE_ACTIVATION"></span><span id="vm_e_pref_unloadable_activation"></span>**VM\_E\_PREF\_UNLOADABLE\_ACTIVATION**
</dt> <dd> <dl> <dt>

0xA0040306
</dt> <dt>



The activation dictionary could not be loaded. This can be caused by a corrupted or missing saved state file.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_SAVED_STATE_BAD_VERSION"></span><span id="vm_e_pref_saved_state_bad_version"></span>**VM\_E\_PREF\_SAVED\_STATE\_BAD\_VERSION**
</dt> <dd> <dl> <dt>

0xA0040307
</dt> <dt>



The virtual machine's saved state is not compatible with this version of Virtual Server.


</dt> </dl> </dd> <dt>

<span id="VM_E_PREF_SAVED_STATE_ACCESS_DENIED"></span><span id="vm_e_pref_saved_state_access_denied"></span>**VM\_E\_PREF\_SAVED\_STATE\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

0xA0040308
</dt> <dt>



The virtual machine's saved state could not be accessed because the user has insufficient access rights.


</dt> </dl> </dd> <dt>

<span id="VM_E_CONFIG_NO_NAME"></span><span id="vm_e_config_no_name"></span>**VM\_E\_CONFIG\_NO\_NAME**
</dt> <dd> <dl> <dt>

0xA0040400
</dt> <dt>



A virtual machine name was not specified.


</dt> </dl> </dd> <dt>

<span id="VM_E_CONFIG_NAME_TOO_LONG"></span><span id="vm_e_config_name_too_long"></span>**VM\_E\_CONFIG\_NAME\_TOO\_LONG**
</dt> <dd> <dl> <dt>

0xA0040401
</dt> <dt>



The name of the virtual machine is too long. The length of the name cannot be more than 256 characters.


</dt> </dl> </dd> <dt>

<span id="VM_E_CONFIG_NAME_INVALID_CHAR"></span><span id="vm_e_config_name_invalid_char"></span>**VM\_E\_CONFIG\_NAME\_INVALID\_CHAR**
</dt> <dd> <dl> <dt>

0xA0040402
</dt> <dt>



The name of the virtual machine contains an invalid character (one of "\*?:&lt;&gt;/\|\\"").


</dt> </dl> </dd> <dt>

<span id="VM_E_CONFIG_DUPLICATE_NAME"></span><span id="vm_e_config_duplicate_name"></span>**VM\_E\_CONFIG\_DUPLICATE\_NAME**
</dt> <dd> <dl> <dt>

0xA0040403
</dt> <dt>



A virtual machine with this name already exists.


</dt> </dl> </dd> <dt>

<span id="VM_E_VM_RUNNING"></span><span id="vm_e_vm_running"></span>**VM\_E\_VM\_RUNNING**
</dt> <dd> <dl> <dt>

0xA0040500
</dt> <dt>



Operation cannot be performed on a running virtual machine.


</dt> </dl> </dd> <dt>

<span id="VM_E_VM_NO_SAVED_STATE"></span><span id="vm_e_vm_no_saved_state"></span>**VM\_E\_VM\_NO\_SAVED\_STATE**
</dt> <dd> <dl> <dt>

0xA0040501
</dt> <dt>



Attempt to restore a virtual machine with no saved state.


</dt> </dl> </dd> <dt>

<span id="VM_E_DRIVE_INVALID"></span><span id="vm_e_drive_invalid"></span>**VM\_E\_DRIVE\_INVALID**
</dt> <dd> <dl> <dt>

0xA0040502
</dt> <dt>



Invalid drive was specified.


</dt> </dl> </dd> <dt>

<span id="VM_E_DRIVE_BUS_LOC_IN_USE"></span><span id="vm_e_drive_bus_loc_in_use"></span>**VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**
</dt> <dd> <dl> <dt>

0xA0040503
</dt> <dt>



Attempt to attach a drive to a bus location that is already in use.


</dt> </dl> </dd> <dt>

<span id="VM_E_ADDITIONS_NOT_AVAIL"></span><span id="vm_e_additions_not_avail"></span>**VM\_E\_ADDITIONS\_NOT\_AVAIL**
</dt> <dd> <dl> <dt>

0xA0040504
</dt> <dt>



Additions are not installed in this virtual machine, or the virtual machine has never been started.


</dt> </dl> </dd> <dt>

<span id="VM_E_ADDITIONS_FEATURE_NOT_AVAIL"></span><span id="vm_e_additions_feature_not_avail"></span>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**
</dt> <dd> <dl> <dt>

0xA0040505
</dt> <dt>



Additions feature is not available; either Additions are not installed or the feature has been disabled.


</dt> </dl> </dd> <dt>

<span id="VM_E_FOLDER_NOT_SHARED"></span><span id="vm_e_folder_not_shared"></span>**VM\_E\_FOLDER\_NOT\_SHARED**
</dt> <dd> <dl> <dt>

0xA0040506
</dt> <dt>



The specified folder is not being shared by the Additions.


</dt> </dl> </dd> <dt>

<span id="VM_E_VM_PAUSED"></span><span id="vm_e_vm_paused"></span>**VM\_E\_VM\_PAUSED**
</dt> <dd> <dl> <dt>

0xA0040507
</dt> <dt>



Cannot execute a command in the guest because the virtual machine is paused.


</dt> </dl> </dd> <dt>

<span id="VM_E_MEDIA_UNMOUNT_FAIL"></span><span id="vm_e_media_unmount_fail"></span>**VM\_E\_MEDIA\_UNMOUNT\_FAIL**
</dt> <dd> <dl> <dt>

0xA0040508
</dt> <dt>



Attempt to unmount the media present in virtual machine DVD drive failed.


</dt> </dl> </dd> <dt>

<span id="VM_E_IMAGE_CAPTURE_FAIL"></span><span id="vm_e_image_capture_fail"></span>**VM\_E\_IMAGE\_CAPTURE\_FAIL**
</dt> <dd> <dl> <dt>

0xA0040650
</dt> <dt>



Could not capture floppy drive image.


</dt> </dl> </dd> <dt>

<span id="VM_E_HOST_FLOPPY_CAPTURE_FAIL"></span><span id="vm_e_host_floppy_capture_fail"></span>**VM\_E\_HOST\_FLOPPY\_CAPTURE\_FAIL**
</dt> <dd> <dl> <dt>

0xA0040651
</dt> <dt>



Could not capture host floppy drive.


</dt> </dl> </dd> <dt>

<span id="VM_E_NO_MEDIA_CAPTURED"></span><span id="vm_e_no_media_captured"></span>**VM\_E\_NO\_MEDIA\_CAPTURED**
</dt> <dd> <dl> <dt>

0xA0040652
</dt> <dt>



Could not capture floppy drive image.


</dt> </dl> </dd> <dt>

<span id="VM_E_PARENT_PATH_NOT_FOUND"></span><span id="vm_e_parent_path_not_found"></span>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0xA0040677
</dt> <dt>



Invalid differencing drive parent path.


</dt> </dl> </dd> <dt>

<span id="VM_E_FILE_TOO_LARGE_FOR_VOLUME"></span><span id="vm_e_file_too_large_for_volume"></span>**VM\_E\_FILE\_TOO\_LARGE\_FOR\_VOLUME**
</dt> <dd> <dl> <dt>

0xA0040679
</dt> <dt>



Attempt to create a file larger than what the host volume supports.


</dt> </dl> </dd> <dt>

<span id="VM_E_FILE_READ_ONLY"></span><span id="vm_e_file_read_only"></span>**VM\_E\_FILE\_READ\_ONLY**
</dt> <dd> <dl> <dt>

0xA004067A
</dt> <dt>



The file cannot be read-only.


</dt> </dl> </dd> <dt>

<span id="VM_E_WRONG_HD_IMAGE_TYPE"></span><span id="vm_e_wrong_hd_image_type"></span>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**
</dt> <dd> <dl> <dt>

0xA004067B
</dt> <dt>



The hard disk drive image type cannot be used for this operation.


</dt> </dl> </dd> <dt>

<span id="VM_E_HD_IMAGE_OPEN_FAIL"></span><span id="vm_e_hd_image_open_fail"></span>**VM\_E\_HD\_IMAGE\_OPEN\_FAIL**
</dt> <dd> <dl> <dt>

0xA004067C
</dt> <dt>



The hard disk drive image could not be opened. Make sure that the file still exists and is not in use by any other applications.


</dt> </dl> </dd> <dt>

<span id="VM_E_HOST_DRIVE_NOT_FOUND"></span><span id="vm_e_host_drive_not_found"></span>**VM\_E\_HOST\_DRIVE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0xA004067E
</dt> <dt>



The host drive linked to by this virtual hard disk image cannot be found. Make sure that the host drive for this virtual hard disk image still exists.


</dt> </dl> </dd> <dt>

<span id="VM_E_HD_IMAGE_ACCESS"></span><span id="vm_e_hd_image_access"></span>**VM\_E\_HD\_IMAGE\_ACCESS**
</dt> <dd> <dl> <dt>

0xA0040681
</dt> <dt>



An unknown error has occurred attempting to access a virtual hard disk image.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_HD_FILE"></span><span id="vm_e_invalid_hd_file"></span>**VM\_E\_INVALID\_HD\_FILE**
</dt> <dd> <dl> <dt>

0xA0040682
</dt> <dt>



The virtual hard disk image seems to be invalid. Make sure that the file has the "".vhd"" virtual hard disk image extension and that the file is actually a virtual hard disk image.


</dt> </dl> </dd> <dt>

<span id="VM_E_IMAGE_SIZE_TOO_LARGE"></span><span id="vm_e_image_size_too_large"></span>**VM\_E\_IMAGE\_SIZE\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

0xA0040683
</dt> <dt>



A virtual hard disk image size cannot be larger than 2,088,960 MB. A FAT16 virtual hard disk image size cannot be greater than 2,000 MB.


</dt> </dl> </dd> <dt>

<span id="VM_E_IMAGE_SIZE_TOO_SMALL"></span><span id="vm_e_image_size_too_small"></span>**VM\_E\_IMAGE\_SIZE\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

0xA0040684
</dt> <dt>



An unformatted virtual hard disk image size must be at least 3 MB. A FAT16 virtual hard disk image size must be at least 3 MB. A FAT32 virtual hard disk image size must be at least 514 MB.


</dt> </dl> </dd> <dt>

<span id="VM_E_PARENT_CHILD_ID_MISMATCH"></span><span id="vm_e_parent_child_id_mismatch"></span>**VM\_E\_PARENT\_CHILD\_ID\_MISMATCH**
</dt> <dd> <dl> <dt>

0xA0040685
</dt> <dt>



A differencing drive must be linked to the parent it was created with. If the parent virtual hard disk image was replaced, it could lead to the child pointing at the wrong virtual hard disk image. Make sure to keep the correct child paired with the correct parent.


</dt> </dl> </dd> <dt>

<span id="VM_E_ADAPTER_NOT_FOUND"></span><span id="vm_e_adapter_not_found"></span>**VM\_E\_ADAPTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0xA0040700
</dt> <dt>



Host Ethernet adapter does not exist.


</dt> </dl> </dd> <dt>

<span id="VM_E_VIRTUAL_NETWORK_NAME_ALREADY_EXISTS"></span><span id="vm_e_virtual_network_name_already_exists"></span>**VM\_E\_VIRTUAL\_NETWORK\_NAME\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

0xA0040701
</dt> <dt>



A duplicate virtual network name was specified.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_VIRTUAL_NETWORK_ID"></span><span id="vm_e_invalid_virtual_network_id"></span>**VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID**
</dt> <dd> <dl> <dt>

0xA0040702
</dt> <dt>



A virtual network with the given ID could not be found.


</dt> </dl> </dd> <dt>

<span id="VM_E_CANT_SET_ETHERNET_ADDRESS"></span><span id="vm_e_cant_set_ethernet_address"></span>**VM\_E\_CANT\_SET\_ETHERNET\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA0040703
</dt> <dt>



A virtual NIC Ethernet address cannot be set if the NIC has a dynamic Ethernet address. To set the Ethernet address, first set the [**IVMNetworkAdapter::IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) property to **FALSE**.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_IP_ADDRESS"></span><span id="vm_e_invalid_ip_address"></span>**VM\_E\_INVALID\_IP\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA0040704
</dt> <dt>



The IP address string is not formed correctly. A properly formed IP address follows the pattern ""X.X.X.X"", where 0 &lt;= X &lt;= 255.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_NETWORK_ADDRESS"></span><span id="vm_e_invalid_network_address"></span>**VM\_E\_INVALID\_NETWORK\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA0040705
</dt> <dt>



The IP address string must be a class A, class B, or class C address.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_NETWORK_MASK"></span><span id="vm_e_invalid_network_mask"></span>**VM\_E\_INVALID\_NETWORK\_MASK**
</dt> <dd> <dl> <dt>

0xA0040706
</dt> <dt>



The network mask is not valid for the class of network address.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_STARTING_ADDRESS"></span><span id="vm_e_invalid_starting_address"></span>**VM\_E\_INVALID\_STARTING\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA0040707
</dt> <dt>



The starting IP address is not in a valid range.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_ENDING_ADDRESS"></span><span id="vm_e_invalid_ending_address"></span>**VM\_E\_INVALID\_ENDING\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA0040708
</dt> <dt>



The ending IP address is not in a valid range.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_ADDRESS_RANGE"></span><span id="vm_e_invalid_address_range"></span>**VM\_E\_INVALID\_ADDRESS\_RANGE**
</dt> <dd> <dl> <dt>

0xA0040709
</dt> <dt>



The starting IP address must be less than the ending IP address.


</dt> </dl> </dd> <dt>

<span id="VM_E_CANT_SET_DYNAMIC_MAC_ADDRESS"></span><span id="vm_e_cant_set_dynamic_mac_address"></span>**VM\_E\_CANT\_SET\_DYNAMIC\_MAC\_ADDRESS**
</dt> <dd> <dl> <dt>

0xA004070A
</dt> <dt>



The Ethernet address for a network interface can either be generated dynamically by virtual server or can be set to a static address by the user. This function cannot be called when the address is set to be generated dynamically. The function [**IVMNetworkAdapter::IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) is used to change the generation behavior of the Ethernet address.


</dt> </dl> </dd> <dt>

<span id="VM_E_DRIVE_IN_USE"></span><span id="vm_e_drive_in_use"></span>**VM\_E\_DRIVE\_IN\_USE**
</dt> <dd> <dl> <dt>

0xA0040727
</dt> <dt>



Access to the requested drive failed because the drive is already in use.


</dt> </dl> </dd> <dt>

<span id="VM_E_MEDIA_WRONG_TYPE"></span><span id="vm_e_media_wrong_type"></span>**VM\_E\_MEDIA\_WRONG\_TYPE**
</dt> <dd> <dl> <dt>

0xA0040728
</dt> <dt>



The media that is currently captured by this drive does not match the type that is required for the requested operation.


</dt> </dl> </dd> <dt>

<span id="VM_E_NO_LICENSE"></span><span id="vm_e_no_license"></span>**VM\_E\_NO\_LICENSE**
</dt> <dd> <dl> <dt>

0xA0040750
</dt> <dt>



No license is available.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_LICENSE"></span><span id="vm_e_invalid_license"></span>**VM\_E\_INVALID\_LICENSE**
</dt> <dd> <dl> <dt>

0xA0040751
</dt> <dt>



An invalid license is installed.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_LICENSE_KEY"></span><span id="vm_e_invalid_license_key"></span>**VM\_E\_INVALID\_LICENSE\_KEY**
</dt> <dd> <dl> <dt>

0xA0040752
</dt> <dt>



An invalid license key was found.


</dt> </dl> </dd> <dt>

<span id="VM_E_INVALID_LICENSE_VALUE"></span><span id="vm_e_invalid_license_value"></span>**VM\_E\_INVALID\_LICENSE\_VALUE**
</dt> <dd> <dl> <dt>

0xA0040753
</dt> <dt>



An invalid license value was found.


</dt> </dl> </dd> <dt>

<span id="VM_E_LICENSE_ACTIVE_VM_LIMIT"></span><span id="vm_e_license_active_vm_limit"></span>**VM\_E\_LICENSE\_ACTIVE\_VM\_LIMIT**
</dt> <dd> <dl> <dt>

0xA0040754
</dt> <dt>



Current limit on active virtual machines has been reached.


</dt> </dl> </dd> <dt>

<span id="VM_E_LICENSE_HOST_MEMORY_LIMIT"></span><span id="vm_e_license_host_memory_limit"></span>**VM\_E\_LICENSE\_HOST\_MEMORY\_LIMIT**
</dt> <dd> <dl> <dt>

0xA0040755
</dt> <dt>



Current limit on host memory has been reached.


</dt> </dl> </dd> <dt>

<span id="VM_E_LICENSE_VM_MEMORY_LIMIT"></span><span id="vm_e_license_vm_memory_limit"></span>**VM\_E\_LICENSE\_VM\_MEMORY\_LIMIT**
</dt> <dd> <dl> <dt>

0xA0040756
</dt> <dt>



Current limit on virtual machine memory has been reached.


</dt> </dl> </dd> <dt>

<span id="VM_E_NOT_A_TRIAL_VERSION"></span><span id="vm_e_not_a_trial_version"></span>**VM\_E\_NOT\_A\_TRIAL\_VERSION**
</dt> <dd> <dl> <dt>

0xA0040757
</dt> <dt>



Attempt to invoke trial license routines on a license that is not a trial license.


</dt> </dl> </dd> <dt>

<span id="VM_E_NON_ACTIVE_TRIAL"></span><span id="vm_e_non_active_trial"></span>**VM\_E\_NON\_ACTIVE\_TRIAL**
</dt> <dd> <dl> <dt>

0xA0040758
</dt> <dt>



The trial license installed either has not yet started or is already finished.


</dt> </dl> </dd> <dt>

<span id="VM_E_MOUSE_NOT_ACTIVE"></span><span id="vm_e_mouse_not_active"></span>**VM\_E\_MOUSE\_NOT\_ACTIVE**
</dt> <dd> <dl> <dt>

0xA0040800
</dt> <dt>



The mouse device has not been powered up in the guest.


</dt> </dl> </dd> <dt>

<span id="VM_E_USING_ABSOLUTE_COORDINATES"></span><span id="vm_e_using_absolute_coordinates"></span>**VM\_E\_USING\_ABSOLUTE\_COORDINATES**
</dt> <dd> <dl> <dt>

0xA0040801
</dt> <dt>



The mouse device is currently set to use absolute mouse coordinates.


</dt> </dl> </dd> <dt>

<span id="VM_E_USING_RELATIVE_COORDINATES"></span><span id="vm_e_using_relative_coordinates"></span>**VM\_E\_USING\_RELATIVE\_COORDINATES**
</dt> <dd> <dl> <dt>

0xA0040802
</dt> <dt>



The mouse device is currently set to use relative mouse coordinates.


</dt> </dl> </dd> <dt>

<span id="VM_E_SET_EXCLUSIVE_MODE_FAIL"></span><span id="vm_e_set_exclusive_mode_fail"></span>**VM\_E\_SET\_EXCLUSIVE\_MODE\_FAIL**
</dt> <dd> <dl> <dt>

0xA0040825
</dt> <dt>



Failed to set or release exclusive mode as requested. This could be because the virtual machine is no longer running, or because another process has already acquired exclusive mode on the virtual machine's keyboard device.


</dt> </dl> </dd> <dt>

<span id="VM_E_NO_DISPLAY"></span><span id="vm_e_no_display"></span>**VM\_E\_NO\_DISPLAY**
</dt> <dd> <dl> <dt>

0xA0040850
</dt> <dt>



Failed to find the video device for a virtual machine.


</dt> </dl> </dd> <dt>

<span id="VM_E_SECURITY_DUPLICATE_USER"></span><span id="vm_e_security_duplicate_user"></span>**VM\_E\_SECURITY\_DUPLICATE\_USER**
</dt> <dd> <dl> <dt>

0xA0040900
</dt> <dt>



An attempt was made to add a duplicate user or group to a security object.


</dt> </dl> </dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 






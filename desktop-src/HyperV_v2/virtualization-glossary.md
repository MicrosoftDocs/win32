---
description: Glossary of terms used in the Windows Virtualization SDK documentation.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 365D0295-EA0B-4B40-8272-DFF62B2A6F3D
title: Hyper-V glossary
ms.topic: article
ms.date: 05/31/2018
---

# Hyper-V glossary

This topic provides a glossary of terms used in the Windows Virtualization SDK documentation.

<dl> <dt>

<span id="hyperv.virtualization_glossary_binding"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_BINDING"></span>**binding**
</dt> <dd>

A process by which software services and layers are linked together. When a network service is installed, the binding relationships and dependencies for the services are established.

</dd> <dt>

<span id="hyperv.virtualization_glossary_checkpoint"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_CHECKPOINT"></span>**checkpoint**
</dt> <dd>

A snapshot of a virtual machine that enables an administrator to roll the virtual machine back to its state at the moment the checkpoint was created.

</dd> <dt>

<span id="hyperv.virtualization_glossary_compact"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_COMPACT"></span>**compact**
</dt> <dd>

To reduce the size of a dynamically expanding virtual hard disk by removing unused space from the .vhd file.

</dd> <dt>

<span id="hyperv.virtualization_glossary_dvhd"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_DVHD"></span>**differencing virtual hard disk**
</dt> <dd>

A virtual hard disk that stores the changes to an associated parent virtual hard disk for the purpose of keeping the parent intact. The differencing disk is a separate .vhd file that is associated with the .vhd file of the parent disk. Changes continue to accumulate in the differencing disk until it is merged to the parent disk.

</dd> <dt>

<span id="hyperv.virtualization_glossary_devhd"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_DEVHD"></span>**dynamically expanding virtual hard disk**
</dt> <dd>

A virtual hard disk that grows in size each time it is modified. This type of virtual hard disk starts as a 3 KB .vhd file and can grow as large as the maximum size specified when the file was created. The only way to reduce the file size is to zero out the deleted data and then compact the virtual hard disk.

</dd> <dt>

<span id="hyperv.virtualization_glossary_fvhd"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_FVHD"></span>**fixed-size virtual hard disk**
</dt> <dd>

A virtual hard disk with a fixed size that is determined and for which all space is allocated when the disk is created. The size of the disk does not change when data is added or deleted.

</dd> <dt>

<span id="hyperv.virtualization_glossary_gen1vm"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_GEN1VM"></span>**Generation 1 virtual machine**
</dt> <dd>

A virtual machine (VM) that contains the same virtual hardware present in versions of Hyper-V prior to Windows 8.1 and Windows Server 2012 R2

</dd> <dt>

<span id="hyperv.virtualization_glossary_gen2vm"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_GEN2VM"></span>**Generation 2 virtual machine**
</dt> <dd>

A virtual machine (VM) that contains a simplified virtual hardware model and uses UEFI firmware instead of BIOS. In this VM, most of the emulated devices are removed, which reduces management complexity and security attack surface.

</dd> <dt>

<span id="hyperv.virtualization_glossary_guestos"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_GUESTOS"></span>**guest operating system**
</dt> <dd>

The operating system running on a virtual machine.

</dd> <dt>

<span id="hyperv.virtualization_glossary_integration_services"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_INTEGRATION_SERVICES"></span>**integration services**
</dt> <dd>

A collection of services and software drivers that maximize performance and provide a better user experience within a virtual machine. Integration services are only available for supported guest operating systems.

</dd> <dt>

<span id="hyperv.virtualization_glossary_kvp"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_KVP"></span>**key-value pair**
</dt> <dd>

A set of data items that contains a unique identifier, called a key, and a value that is the actual data for the key.

</dd> <dt>

<span id="hyperv.virtualization_glossary_physical_computer"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_PHYSICAL_COMPUTER"></span>**physical computer**
</dt> <dd>

A hardware-based computer, as opposed to a software-based virtual machine.

</dd> <dt>

<span id="hyperv.virtualization_glossary_saved_state"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_SAVED_STATE"></span>**saved state**
</dt> <dd>

A manner of storing a virtual machine so that it can be quickly resumed, similar to a hibernated laptop. When you place a running virtual machine in a saved state, Virtual Server and Hyper-V stop the virtual machine, write the data that exists in memory to temporary files, and stop the consumption of system resources. Restoring a virtual machine from a saved state returns it to the same condition it was in when its state was saved.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vfd"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VFD"></span>**virtual floppy disk**
</dt> <dd>

A file-based version of a physical floppy disk. A virtual floppy disk is stored as a file with a .vfd file name extension.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vhd"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VHD"></span>**virtual hard disk**
</dt> <dd>

The storage medium for a virtual machine. It can reside on any storage topology that the host operating system can access, including external devices, storage area networks, and network-attached storage. The file name extension is .vhd.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vm"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VM"></span>**virtual machine**
</dt> <dd>

A computer within a computer, implemented in software. A virtual machine emulates a complete hardware system, from processor to network card, in a self-contained, isolated software environment, enabling the simultaneous operation of otherwise incompatible operating systems. Each child operating system runs in its own isolated software virtual machine.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vm_config"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VM_CONFIG"></span>**virtual machine configuration**
</dt> <dd>

The configuration of the resources assigned to a virtual machine. Examples include devices such as disks and network adapters, as well as memory and processors.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vmms"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VMMS"></span>**Virtual Machine Management Service**
</dt> <dd>

The Hyper-V service that provides management access to virtual machines.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vmss"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VMSS"></span>**virtual machine snapshot**
</dt> <dd>

A file-based snapshot of the state, disk data, and configuration of a virtual machine at a specific point in time.

</dd> <dt>

<span id="hyperv.virtualization_glossary_virtual_network"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VIRTUAL_NETWORK"></span>**virtual network**
</dt> <dd>

A virtual version of a physical network switch. A virtual network can be configured to provide access to local or external network resources for one or more virtual machines.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vnm"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VNM"></span>**Virtual Network Manager**
</dt> <dd>

A Hyper-V service used to create and manage virtual networks.

</dd> <dt>

<span id="hyperv.virtualization_glossary_virtual_switch"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VIRTUAL_SWITCH"></span>**virtual switch**
</dt> <dd>

See virtual network.

</dd> <dt>

<span id="hyperv.virtualization_glossary_vhdx_resize"></span><span id="HYPERV.VIRTUALIZATION_GLOSSARY_VHDX_RESIZE"></span>**VHDX resize**
</dt> <dd>

The operation that shrinks or expands a virtual hard disk.

</dd> </dl>

 

 




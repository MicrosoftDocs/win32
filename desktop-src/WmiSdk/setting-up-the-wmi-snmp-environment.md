---
description: Communicating with a network device using the WMI SNMP interface requires the configuration of the device, SNMP, and WMI services. The information in this topic explains how to set up the WMI SNMP environment.
ms.assetid: 8074175a-af66-49b2-9723-dfb38a08fb63
ms.tgt_platform: multiple
title: Setting up the WMI SNMP Environment
ms.topic: article
ms.date: 05/31/2018
---

# Setting up the WMI SNMP Environment

Communicating with a network device using the WMI SNMP interface requires the configuration of the device, SNMP, and WMI services. The information in this topic explains how to set up the WMI SNMP environment.

The following sections are discussed in this topic:

## Installing the SNMP Provider

The SNMP service is not enabled by default. You can enable the SNMP service and the WMI SNMP Provider through the Control Panel. Be aware that the SNMP service must be enabled and running for the WMI SNMP provider to work.

Starting with Windows Vista, use the following procedure to install the SNMP provider.

**To install the SNMP Provider**

1.  From the **Control Panel**, select **Programs**.
2.  Under **Programs and Features**, select **Turn Windows features on or off**.
3.  In the Windows features list, scroll down to **SNMP feature** and expand the list so that you can see **WMI SNMP Provider**.
4.  Select the check box for **WMI SNMP Provider**. The check box for **SNMP feature** is selected automatically because the provider requires SNMP.
5.  Click **OK**.
6.  From a command prompt or the **Start** menu, run Services.msc and ensure that the SNMP service is started.

## Creating an SNMP Namespace

An SNMP namespace defines a view of a network device.

> [!Note]  
> For more information about support and installation of this component on a specific operating system, see [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md).

 

The following procedure describes how to create an SNMP WMI [*namespace*](gloss-n.md).

**To create an SNMP namespace**

1.  Create an instance of the [**\_\_Namespace**](--namespace.md) system class either by compiling a [*Managed Object Format*](gloss-m.md) .mof file or by using the [COM API for WMI](com-api-for-wmi.md).

    For more information, see [Creating Hierarchies Within WMI](creating-hierarchies-within-wmi.md).

2.  Associate SNMP provider [*qualifiers*](gloss-q.md) with the namespace definition.

    The SNMP provider qualifiers contain implementation-specific context information and transport properties that define how the SNMP provider accesses an SNMP device. For more information, see [**Qualifiers Specific to the SNMP Provider**](qualifiers-specific-to-the-snmp-provider.md).

3.  Use the [mofcomp](mofcomp.md) command line tool to load the MOF code into the WMI repository.

    For more information, see [Compiling MOF files](compiling-mof-files.md).

The following MOF code example defines the \\snmp namespace with a subset of the qualifiers that can be associated with an SNMP namespace.

``` syntax
// Load classes and instances into <\\.\root> namespace

#pragma namespace("\\\\.\\root")               

[ 
  AgentAddress( "localhost" ), 
  AgentReadCommunityName( "public"), 
  AgentWriteCommunityName( "private"), 
  AgentRetryCount( 1 ), 
  AgentRetryTimeout( 500 ), 
  AgentVarBindsPerPdu( 10 ),
  AgentFlowControlWindowSize ( 3 ) 
]

  instance of __Namespace
  {
      Name = "snmp" ;
  };
```

## Inserting SNMP MIB Data into WMI

As a provider, the SNMP provider acts as a bridge between SNMP data and WMI classes. Therefore, you must have classes in WMI that represent different aspects of an SNMP-enabled device. To do so, you must use the SNMP information module compiler ([smi2smir](smi2smir.md)) to compile SNMP management information from the SNMP format into the equivalent CIM schema definitions. You can then direct the output of the information compiler into an SNMP schema database called the "SNMP Module Information Repository (SMIR)" or to several different kinds of MOF files.

The compiler runs in the command-line mode, using one MIB file as input. The following command loads the specified MIB file into the SMIR.

**smi2smir /a** *\<MIB file>*

## Setting Up SNMP Communities

As a security measure, the SNMP "public" community is not created by default. You can create the community as described in [Communities Registry Settings](/previous-versions/windows/embedded/ms907028(v=msdn.10)). If you do not have any community, then create the "public" community to access the SNMP provider.

## Generating MOF Files from MIB Files

The following commands are an example of how to generate MOF files from the MIB files that are installed when the SNMP provider is installed.

**cd** *%windir%\\system32\\wbem\\SNMP*

**Smi2smir /g** *..\\..\\hostmib.mib* **>** *hostmib.mof*

**Smi2smir /g** *..\\..\\ipforwd.mib* **>** *ipforwd.mof*

**Smi2smir /g** *..\\..\\nipx.mib* **>** *nipx.mof*

**Smi2smir /g** *..\\..\\mib\_ii.mib* **>** *mib\_ii.mof*

**Smi2smir /g** *..\\..\\lmmib2.mib* **>** *lmmib2.mof*

**Smi2smir /g** *..\\..\\mcastmib.mib* **>** *mcastmib.mof*

**Smi2smir /g** *..\\..\\rfc2571.mib* **>** *rfc2571.mof*

**Smi2smir /g** *..\\..\\wfospf.mib* **>** *wfospf.mof*

**Smi2smir /g** *..\\..\\dhcp.mib..\\..\\msft.mib* **>** *dhcp.mof*

**Smi2smir /g** *..\\..\\wins.mib..\\..\\msft.mib* **>** *wins.mof*

**Smi2smir /g** *..\\..\\mipx.mib..\\..\\msft.mib* **>** *mipx.mof*

**Smi2smir /g** *..\\..\\mripsap.mib..\\..\\msft.mib* **>** *mripsap.mof*

**Smi2smir /g** *..\\..\\msipbtp.mib..\\..\\msft.mib* **>** *msipbtp.mof*

**Smi2smir /g** *..\\..\\msiprip2.mib..\\..\\msft.mib* **>** *msiprip2.mof*

## Adding SNMP MOF Files to the WMI Repository

The following commands are an example of how to add the MOF files that are generated from the MIB files to the WMI repository. If you want to add the MOF files to the list of files to be automatically restored in a [*WMI repository*](gloss-w.md) recovery, add the **-AUTORECOVER** flag to the end of each command. For more information about the WMI Mofcomp.exe command-line tool, see [**mofcomp**](mofcomp.md).

**mofcomp** *hostmib.mof*

**mofcomp** *ipforwd.mof*

**mofcomp** *nipx.mof*

**mofcomp** *mib\_ii.mof*

**mofcomp** *lmmib2.mof*

**mofcomp** *mcastmib.mof*

**mofcomp** *rfc2571.mof*

**mofcomp** *wfospf.mof*

**mofcomp** *dhcp.mof*

**mofcomp** *mipx.mof*

**mofcomp** *mripsap.mof*

**mofcomp** *msipbtp.mof*

**mofcomp** *msiprip2.mof*

## Related topics

<dl> <dt>

[Accessing SNMP Devices](accessing-snmp-devices.md)
</dt> </dl>

 

 

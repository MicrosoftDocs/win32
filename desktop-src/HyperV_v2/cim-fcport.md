---
description: Represents the capabilities and management of a fibre channel (FC) port device.
ms.assetid: 32a11971-9e18-410d-a3cd-4921a7e986f0
title: CIM_FCPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_FCPort
- CIM_FCPort.PortType
- CIM_FCPort.SupportedCOS
- CIM_FCPort.ActiveCOS
- CIM_FCPort.SupportedFC4Types
- CIM_FCPort.ActiveFC4Types
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_FCPort class

> [!NOTE]
> This article contains references to the term slave, a term that Microsoft no longer uses. When the term is removed from the software, we’ll remove it from this article.

Represents the capabilities and management of a fibre channel (FC) port device.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Device::FC"), AMENDMENT]
class CIM_FCPort : CIM_NetworkPort
{
  uint16 PortType;
  uint16 SupportedCOS[];
  uint16 ActiveCOS[];
  uint16 SupportedFC4Types[];
  uint16 ActiveFC4Types[];
};
```

## Members

> [!NOTE]
> This article contains references to the term slave, a term that Microsoft no longer uses. When the term is removed from the software, we’ll remove it from this article.

The **CIM\_FCPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_FCPort** class has these properties.

<dl> <dt>

**ActiveCOS**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_FCPort**.**SupportedCOS**")
</dt> </dl>

The active class of service (COS) settings for the fibre channel.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (2)


</dt> <dd></dd> <dt>

<span id="3"></span>

**3** (3)


</dt> <dd></dd> <dt>

<span id="4"></span>

**4** (4)


</dt> <dd></dd> <dt>

<span id="5"></span>

**5** (5)


</dt> <dd></dd> <dt>

<span id="6"></span>

**6** (6)


</dt> <dd></dd> <dt>

<span id="F"></span><span id="f"></span>

**F** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**ActiveFC4Types**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_FCPort**.**SupportedFC4Types**")
</dt> </dl>

The FC-4 protocols that are running on the fibre channel.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="ISO_IEC_8802_-_2_LLC"></span><span id="iso_iec_8802_-_2_llc"></span>

**ISO/IEC 8802 - 2 LLC** (4)


</dt> <dd></dd> <dt>

<span id="IP_over_FC"></span><span id="ip_over_fc"></span><span id="IP_OVER_FC"></span>

**IP over FC** (5)


</dt> <dd></dd> <dt>

<span id="SCSI_-_FCP"></span><span id="scsi_-_fcp"></span>

**SCSI - FCP** (8)


</dt> <dd></dd> <dt>

<span id="SCSI_-_GPP"></span><span id="scsi_-_gpp"></span>

**SCSI - GPP** (9)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Master"></span><span id="ipi_-_3_master"></span><span id="IPI_-_3_MASTER"></span>

**IPI - 3 Master** (17)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Slave"></span><span id="ipi_-_3_slave"></span><span id="IPI_-_3_SLAVE"></span>

**IPI - 3 Slave** (18)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Peer"></span><span id="ipi_-_3_peer"></span><span id="IPI_-_3_PEER"></span>

**IPI - 3 Peer** (19)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Master"></span><span id="cp_ipi_-_3_master"></span><span id="CP_IPI_-_3_MASTER"></span>

**CP IPI - 3 Master** (21)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Slave"></span><span id="cp_ipi_-_3_slave"></span><span id="CP_IPI_-_3_SLAVE"></span>

**CP IPI - 3 Slave** (22)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Peer"></span><span id="cp_ipi_-_3_peer"></span><span id="CP_IPI_-_3_PEER"></span>

**CP IPI - 3 Peer** (23)


</dt> <dd></dd> <dt>

<span id="SBCCS_Channel"></span><span id="sbccs_channel"></span><span id="SBCCS_CHANNEL"></span>

**SBCCS Channel** (25)


</dt> <dd></dd> <dt>

<span id="SBCCS_Control_Unit"></span><span id="sbccs_control_unit"></span><span id="SBCCS_CONTROL_UNIT"></span>

**SBCCS Control Unit** (26)


</dt> <dd></dd> <dt>

<span id="FC-SB-2_Channel"></span><span id="fc-sb-2_channel"></span><span id="FC-SB-2_CHANNEL"></span>

**FC-SB-2 Channel** (27)


</dt> <dd></dd> <dt>

<span id="FC-SB-2_Control_Unit"></span><span id="fc-sb-2_control_unit"></span><span id="FC-SB-2_CONTROL_UNIT"></span>

**FC-SB-2 Control Unit** (28)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel_Services__FC-GS__FC-GS-2__FC-GS-3_"></span><span id="fibre_channel_services__fc-gs__fc-gs-2__fc-gs-3_"></span><span id="FIBRE_CHANNEL_SERVICES__FC-GS__FC-GS-2__FC-GS-3_"></span>

**Fibre Channel Services (FC-GS, FC-GS-2, FC-GS-3)** (32)


</dt> <dd></dd> <dt>

<span id="FC-SW"></span><span id="fc-sw"></span>

**FC-SW** (34)


</dt> <dd></dd> <dt>

<span id="FC_-_SNMP"></span><span id="fc_-_snmp"></span>

**FC - SNMP** (36)


</dt> <dd></dd> <dt>

<span id="HIPPI_-_FP"></span><span id="hippi_-_fp"></span>

**HIPPI - FP** (64)


</dt> <dd></dd> <dt>

<span id="BBL_Control"></span><span id="bbl_control"></span><span id="BBL_CONTROL"></span>

**BBL Control** (80)


</dt> <dd></dd> <dt>

<span id="BBL_FDDI_Encapsulated_LAN_PDU"></span><span id="bbl_fddi_encapsulated_lan_pdu"></span><span id="BBL_FDDI_ENCAPSULATED_LAN_PDU"></span>

**BBL FDDI Encapsulated LAN PDU** (81)


</dt> <dd></dd> <dt>

<span id="BBL_802.3_Encapsulated_LAN_PDU"></span><span id="bbl_802.3_encapsulated_lan_pdu"></span><span id="BBL_802.3_ENCAPSULATED_LAN_PDU"></span>

**BBL 802.3 Encapsulated LAN PDU** (82)


</dt> <dd></dd> <dt>

<span id="FC_-_VI"></span><span id="fc_-_vi"></span>

**FC - VI** (88)


</dt> <dd></dd> <dt>

<span id="FC_-_AV"></span><span id="fc_-_av"></span>

**FC - AV** (96)


</dt> <dd></dd> <dt>

<span id="Vendor_Unique"></span><span id="vendor_unique"></span><span id="VENDOR_UNIQUE"></span>

**Vendor Unique** (255)


</dt> <dd></dd> </dl>

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PortType")
</dt> </dl>

The enabled mode for the port. The port modes are defined by ANSI X3 standards. If the port is logged in, this will be the negotiated port type, otherwise the configured port type will be reported.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The related property **OtherPortType** contains a string description of the type of port

</dd> <dt>

<span id="N"></span><span id="n"></span>

<span id="N"></span><span id="n"></span>**N** (10)


</dt> <dd>

Node Port

</dd> <dt>

<span id="NL"></span><span id="nl"></span>

<span id="NL"></span><span id="nl"></span>**NL** (11)


</dt> <dd>

Node Port supporting FC arbitrated loop

</dd> <dt>

<span id="F_NL"></span><span id="f_nl"></span>

<span id="F_NL"></span><span id="f_nl"></span>**F/NL** (12)


</dt> <dd></dd> <dt>

<span id="Nx"></span><span id="nx"></span><span id="NX"></span>

<span id="Nx"></span><span id="nx"></span><span id="NX"></span>**Nx** (13)


</dt> <dd>

Port may negotiate to become either a node port (N) or a node port supporting FC arbitrated loop (NL)

</dd> <dt>

<span id="E"></span><span id="e"></span>

<span id="E"></span><span id="e"></span>**E** (14)


</dt> <dd>

Expansion Port connecting fabric elements (for example, FC switches)

</dd> <dt>

<span id="F"></span><span id="f"></span>

<span id="F"></span><span id="f"></span>**F** (15)


</dt> <dd>

Fabric (element) Port

</dd> <dt>

<span id="FL"></span><span id="fl"></span>

<span id="FL"></span><span id="fl"></span>**FL** (16)


</dt> <dd>

Fabric (element) Port supporting FC arbitrated loop

</dd> <dt>

<span id="B"></span><span id="b"></span>

<span id="B"></span><span id="b"></span>**B** (17)


</dt> <dd>

Bridge port

</dd> <dt>

<span id="G"></span><span id="g"></span>

<span id="G"></span><span id="g"></span>**G** (18)


</dt> <dd>

Port may negotiate to become either an expansion port (E), or a fabric port (F)

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (16000..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedCOS**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The class of service (COS) settings that are supported by the fibre channel.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (2)


</dt> <dd></dd> <dt>

<span id="3"></span>

**3** (3)


</dt> <dd></dd> <dt>

<span id="4"></span>

**4** (4)


</dt> <dd></dd> <dt>

<span id="5"></span>

**5** (5)


</dt> <dd></dd> <dt>

<span id="6"></span>

**6** (6)


</dt> <dd></dd> <dt>

<span id="F"></span><span id="f"></span>

**F** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedFC4Types**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The FC-4 protocols that are supported by the fibre channel.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="ISO_IEC_8802_-_2_LLC"></span><span id="iso_iec_8802_-_2_llc"></span>

**ISO/IEC 8802 - 2 LLC** (4)


</dt> <dd></dd> <dt>

<span id="IP_over_FC"></span><span id="ip_over_fc"></span><span id="IP_OVER_FC"></span>

**IP over FC** (5)


</dt> <dd></dd> <dt>

<span id="SCSI_-_FCP"></span><span id="scsi_-_fcp"></span>

**SCSI - FCP** (8)


</dt> <dd></dd> <dt>

<span id="SCSI_-_GPP"></span><span id="scsi_-_gpp"></span>

**SCSI - GPP** (9)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Master"></span><span id="ipi_-_3_master"></span><span id="IPI_-_3_MASTER"></span>

**IPI - 3 Master** (17)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Slave"></span><span id="ipi_-_3_slave"></span><span id="IPI_-_3_SLAVE"></span>

**IPI - 3 Slave** (18)


</dt> <dd></dd> <dt>

<span id="IPI_-_3_Peer"></span><span id="ipi_-_3_peer"></span><span id="IPI_-_3_PEER"></span>

**IPI - 3 Peer** (19)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Master"></span><span id="cp_ipi_-_3_master"></span><span id="CP_IPI_-_3_MASTER"></span>

**CP IPI - 3 Master** (21)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Slave"></span><span id="cp_ipi_-_3_slave"></span><span id="CP_IPI_-_3_SLAVE"></span>

**CP IPI - 3 Slave** (22)


</dt> <dd></dd> <dt>

<span id="CP_IPI_-_3_Peer"></span><span id="cp_ipi_-_3_peer"></span><span id="CP_IPI_-_3_PEER"></span>

**CP IPI - 3 Peer** (23)


</dt> <dd></dd> <dt>

<span id="SBCCS_Channel"></span><span id="sbccs_channel"></span><span id="SBCCS_CHANNEL"></span>

**SBCCS Channel** (25)


</dt> <dd></dd> <dt>

<span id="SBCCS_Control_Unit"></span><span id="sbccs_control_unit"></span><span id="SBCCS_CONTROL_UNIT"></span>

**SBCCS Control Unit** (26)


</dt> <dd></dd> <dt>

<span id="FC-SB-2_Channel"></span><span id="fc-sb-2_channel"></span><span id="FC-SB-2_CHANNEL"></span>

**FC-SB-2 Channel** (27)


</dt> <dd></dd> <dt>

<span id="FC-SB-2_Control_Unit"></span><span id="fc-sb-2_control_unit"></span><span id="FC-SB-2_CONTROL_UNIT"></span>

**FC-SB-2 Control Unit** (28)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel_Services__FC-GS__FC-GS-2__FC-GS-3_"></span><span id="fibre_channel_services__fc-gs__fc-gs-2__fc-gs-3_"></span><span id="FIBRE_CHANNEL_SERVICES__FC-GS__FC-GS-2__FC-GS-3_"></span>

**Fibre Channel Services (FC-GS, FC-GS-2, FC-GS-3)** (32)


</dt> <dd></dd> <dt>

<span id="FC-SW"></span><span id="fc-sw"></span>

**FC-SW** (34)


</dt> <dd></dd> <dt>

<span id="FC_-_SNMP"></span><span id="fc_-_snmp"></span>

**FC - SNMP** (36)


</dt> <dd></dd> <dt>

<span id="HIPPI_-_FP"></span><span id="hippi_-_fp"></span>

**HIPPI - FP** (64)


</dt> <dd></dd> <dt>

<span id="BBL_Control"></span><span id="bbl_control"></span><span id="BBL_CONTROL"></span>

**BBL Control** (80)


</dt> <dd></dd> <dt>

<span id="BBL_FDDI_Encapsulated_LAN_PDU"></span><span id="bbl_fddi_encapsulated_lan_pdu"></span><span id="BBL_FDDI_ENCAPSULATED_LAN_PDU"></span>

**BBL FDDI Encapsulated LAN PDU** (81)


</dt> <dd></dd> <dt>

<span id="BBL_802.3_Encapsulated_LAN_PDU"></span><span id="bbl_802.3_encapsulated_lan_pdu"></span><span id="BBL_802.3_ENCAPSULATED_LAN_PDU"></span>

**BBL 802.3 Encapsulated LAN PDU** (82)


</dt> <dd></dd> <dt>

<span id="FC_-_VI"></span><span id="fc_-_vi"></span>

**FC - VI** (88)


</dt> <dd></dd> <dt>

<span id="FC_-_AV"></span><span id="fc_-_av"></span>

**FC - AV** (96)


</dt> <dd></dd> <dt>

<span id="Vendor_Unique"></span><span id="vendor_unique"></span><span id="VENDOR_UNIQUE"></span>

**Vendor Unique** (255)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_NetworkPort**](cim-networkport.md)
</dt> </dl>

 


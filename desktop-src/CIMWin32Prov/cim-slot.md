---
description: The CIM\_Slot class represents connectors into which packages are inserted.
ms.assetid: bcb1bdb5-fb1a-47ed-9450-dca38edca0eb
ms.tgt_platform: multiple
title: CIM_Slot class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Slot
- CIM_Slot.Caption
- CIM_Slot.ConnectorPinout
- CIM_Slot.ConnectorType
- CIM_Slot.CreationClassName
- CIM_Slot.Description
- CIM_Slot.HeightAllowed
- CIM_Slot.InstallDate
- CIM_Slot.LengthAllowed
- CIM_Slot.Manufacturer
- CIM_Slot.MaxDataWidth
- CIM_Slot.Model
- CIM_Slot.Name
- CIM_Slot.Number
- CIM_Slot.OtherIdentifyingInfo
- CIM_Slot.PartNumber
- CIM_Slot.PoweredOn
- CIM_Slot.PurposeDescription
- CIM_Slot.SerialNumber
- CIM_Slot.SKU
- CIM_Slot.SpecialPurpose
- CIM_Slot.Status
- CIM_Slot.SupportsHotPlug
- CIM_Slot.Tag
- CIM_Slot.ThermalRating
- CIM_Slot.VccMixedVoltageSupport
- CIM_Slot.Version
- CIM_Slot.VppMixedVoltageSupport
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_Slot class

The **CIM\_Slot** class represents connectors into which packages are inserted. For example, a physical package that is a disk drive can be inserted into an SCA slot, or a card (a subclass of [CIM\_PhysicalPackage](cim-physicalpackage.md)) can be inserted into a 16-, 32-, or 64-bit expansion slot on a hosting board. PCI or PCMCIA Type III Slots are examples of the latter.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{FAF76B86-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_Slot : CIM_PhysicalConnector
{
  string   Caption;
  string   ConnectorPinout;
  uint16   ConnectorType[];
  string   CreationClassName;
  string   Description;
  real32   HeightAllowed;
  datetime InstallDate;
  real32   LengthAllowed;
  string   Manufacturer;
  uint16   MaxDataWidth;
  string   Model;
  string   Name;
  uint16   Number;
  string   OtherIdentifyingInfo;
  string   PartNumber;
  boolean  PoweredOn;
  string   PurposeDescription;
  string   SerialNumber;
  string   SKU;
  boolean  SpecialPurpose;
  string   Status;
  boolean  SupportsHotPlug;
  string   Tag;
  uint32   ThermalRating;
  uint16   VccMixedVoltageSupport[];
  string   Version;
  uint16   VppMixedVoltageSupport[];
};
```

## Members

The **CIM\_Slot** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Slot** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ConnectorPinout**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string that describes the pin configuration and signal use of a physical connector.

This property is inherited from [**CIM\_PhysicalConnector**](cim-physicalconnector.md).

</dd> <dt>

**ConnectorType**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("ConnectorType"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Slot\|004.2")
</dt> </dl>

Type of physical connector. An array is specified to allow the description of combinations of connector information. For example, one array entry could specify RS-232, another DB-25, and a third could define the connector as "Male".

This property is inherited from [**CIM\_PhysicalConnector**](cim-physicalconnector.md).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Other

</dd> <dt>

2
</dt> <dd>

Male

</dd> <dt>

3
</dt> <dd>

Female

</dd> <dt>

4
</dt> <dd>

Shielded

</dd> <dt>

5
</dt> <dd>

Unshielded

</dd> <dt>

6
</dt> <dd>

SCSI (A) High-density (50 pins)

</dd> <dt>

7
</dt> <dd>

SCSI (A) Low-density (50 pins)

</dd> <dt>

8
</dt> <dd>

SCSI (P) High-density (68 pins)

</dd> <dt>

9
</dt> <dd>

SCSI SCA-I (80 pins)

</dd> <dt>

10
</dt> <dd>

SCSI SCA-II (80 pins)

</dd> <dt>

11
</dt> <dd>

SCSI Fibre Channel (DB-9, Copper)

</dd> <dt>

12
</dt> <dd>

SCSI Fibre Channel (Fibre)

</dd> <dt>

13
</dt> <dd>

SCSI Fibre Channel SCA-II (40 pins)

</dd> <dt>

14
</dt> <dd>

SCSI Fibre Channel SCA-II (20 pins)

</dd> <dt>

15
</dt> <dd>

SCSI Fibre Channel BNC

</dd> <dt>

16
</dt> <dd>

ATA 3-1/2 Inch (40 pins)

</dd> <dt>

17
</dt> <dd>

ATA 2-1/2 Inch (44 pins)

</dd> <dt>

18
</dt> <dd>

ATA-2

</dd> <dt>

19
</dt> <dd>

ATA-3

</dd> <dt>

20
</dt> <dd>

ATA/66

</dd> <dt>

21
</dt> <dd>

DB-9

</dd> <dt>

22
</dt> <dd>

DB-15

</dd> <dt>

23
</dt> <dd>

DB-25

</dd> <dt>

24
</dt> <dd>

DB-36

</dd> <dt>

25
</dt> <dd>

RS-232C

</dd> <dt>

26
</dt> <dd>

RS-422

</dd> <dt>

27
</dt> <dd>

RS-423

</dd> <dt>

28
</dt> <dd>

RS-485

</dd> <dt>

29
</dt> <dd>

RS-449

</dd> <dt>

30
</dt> <dd>

V.35

</dd> <dt>

31
</dt> <dd>

X.21

</dd> <dt>

32
</dt> <dd>

IEEE-488

</dd> <dt>

33
</dt> <dd>

AUI

</dd> <dt>

34
</dt> <dd>

UTP Category 3

</dd> <dt>

35
</dt> <dd>

UTP Category 4

</dd> <dt>

36
</dt> <dd>

UTP Category 5

</dd> <dt>

37
</dt> <dd>

BNC

</dd> <dt>

38
</dt> <dd>

RJ11

</dd> <dt>

39
</dt> <dd>

RJ45

</dd> <dt>

40
</dt> <dd>

Fiber MIC

</dd> <dt>

41
</dt> <dd>

Apple AUI

</dd> <dt>

42
</dt> <dd>

Apple GeoPort

</dd> <dt>

43
</dt> <dd>

PCI

</dd> <dt>

44
</dt> <dd>

ISA

</dd> <dt>

45
</dt> <dd>

EISA

</dd> <dt>

46
</dt> <dd>

VESA

</dd> <dt>

47
</dt> <dd>

PCMCIA

</dd> <dt>

48
</dt> <dd>

PCMCIA Type I

</dd> <dt>

49
</dt> <dd>

PCMCIA Type II

</dd> <dt>

50
</dt> <dd>

PCMCIA Type III

</dd> <dt>

51
</dt> <dd>

ZV Port

</dd> <dt>

52
</dt> <dd>

CardBus

</dd> <dt>

53
</dt> <dd>

USB

</dd> <dt>

54
</dt> <dd>

IEEE 1394

</dd> <dt>

55
</dt> <dd>

HIPPI

</dd> <dt>

56
</dt> <dd>

HSSDC (6 pins)

</dd> <dt>

57
</dt> <dd>

GBIC

</dd> <dt>

58
</dt> <dd>

DIN

</dd> <dt>

59
</dt> <dd>

Mini-DIN

</dd> <dt>

60
</dt> <dd>

Micro-DIN

</dd> <dt>

61
</dt> <dd>

PS/2

</dd> <dt>

62
</dt> <dd>

Infrared

</dd> <dt>

63
</dt> <dd>

HP-HIL

</dd> <dt>

64
</dt> <dd>

Access.bus

</dd> <dt>

65
</dt> <dd>

NuBus

</dd> <dt>

66
</dt> <dd>

Centronics

</dd> <dt>

67
</dt> <dd>

Mini-Centronics

</dd> <dt>

68
</dt> <dd>

Mini-Centronics Type-14

</dd> <dt>

69
</dt> <dd>

Mini-Centronics Type-20

</dd> <dt>

70
</dt> <dd>

Mini-Centronics Type-26

</dd> <dt>

71
</dt> <dd>

Bus Mouse

</dd> <dt>

72
</dt> <dd>

ADB

</dd> <dt>

73
</dt> <dd>

AGP

</dd> <dt>

74
</dt> <dd>

VME Bus

</dd> <dt>

75
</dt> <dd>

VME64

</dd> <dt>

76
</dt> <dd>

Proprietary

</dd> <dt>

77
</dt> <dd>

Proprietary Processor Card Slot

</dd> <dt>

78
</dt> <dd>

Proprietary Memory Card Slot

</dd> <dt>

79
</dt> <dd>

Proprietary I/O Riser Slot

</dd> <dt>

80
</dt> <dd>

PCI-66MHZ

</dd> <dt>

81
</dt> <dd>

AGP2X

</dd> <dt>

82
</dt> <dd>

AGP4X

</dd> <dt>

83
</dt> <dd>

PC-98

</dd> <dt>

84
</dt> <dd>

PC-98-Hireso

</dd> <dt>

85
</dt> <dd>

PC-H98

</dd> <dt>

86
</dt> <dd>

PC-98Note

</dd> <dt>

87
</dt> <dd>

PC-98Full

</dd> <dt>

88
</dt> <dd>

SSA SCSI

</dd> <dt>

89
</dt> <dd>

Circular

</dd> <dt>

90
</dt> <dd>

On Board IDE Connector

</dd> <dt>

91
</dt> <dd>

On Board Floppy Connector

</dd> <dt>

92
</dt> <dd>

9 Pin Dual Inline

</dd> <dt>

93
</dt> <dd>

25 Pin Dual Inline

</dd> <dt>

94
</dt> <dd>

50 Pin Dual Inline

</dd> <dt>

95
</dt> <dd>

68 Pin Dual Inline

</dd> <dt>

96
</dt> <dd>

On Board Sound Connector

</dd> <dt>

97
</dt> <dd>

Mini-jack

</dd> <dt>

98
</dt> <dd>

PCI-X

</dd> <dt>

99
</dt> <dd>

Sbus IEEE 1396-1993 32 bit

</dd> <dt>

100
</dt> <dd>

Sbus IEEE 1396-1993 64 bit

</dd> <dt>

101
</dt> <dd>

MCA

</dd> <dt>

102
</dt> <dd>

GIO

</dd> <dt>

103
</dt> <dd>

XIO

</dd> <dt>

104
</dt> <dd>

HIO

</dd> <dt>

105
</dt> <dd>

NGIO

</dd> <dt>

106
</dt> <dd>

PMC

</dd> <dt>

107
</dt> <dd>

MTRJ

</dd> <dt>

108
</dt> <dd>

VF-45

</dd> <dt>

109
</dt> <dd>

Future I/O

</dd> <dt>

110
</dt> <dd>

SC

</dd> <dt>

111
</dt> <dd>

SG

</dd> <dt>

112
</dt> <dd>

Electrical

</dd> <dt>

113
</dt> <dd>

Optical

</dd> <dt>

114
</dt> <dd>

Ribbon

</dd> <dt>

115
</dt> <dd>

GLM

</dd> <dt>

116
</dt> <dd>

1x9

</dd> <dt>

117
</dt> <dd>

Mini SG

</dd> <dt>

118
</dt> <dd>

LC

</dd> <dt>

119
</dt> <dd>

HSSC

</dd> <dt>

120
</dt> <dd>

VHDCI Shielded (68 pins)

</dd> <dt>

121
</dt> <dd>

InfiniBand

</dd> </dl>

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**HeightAllowed**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("inches")
</dt> </dl>

Maximum height, in inches, of an adapter card that can be inserted into the slot.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**LengthAllowed**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("inches")
</dt> </dl>

Maximum length, in inches, of an adapter card that can be inserted into the slot.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Organization that produced the physical element. For more information, see the **Vendor** property of [**CIM\_Product**](cim-product.md).

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**MaxDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Slot\|004.3"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits")
</dt> </dl>

Maximum bus width, in bits, of adapter cards that can be inserted into the slot.

<dt>

<span id="8"></span>

**8** (0)


</dt> <dd></dd> <dt>

<span id="16"></span>

**16** (1)


</dt> <dd></dd> <dt>

<span id="32"></span>

**32** (2)


</dt> <dd></dd> <dt>

<span id="64"></span>

**64** (3)


</dt> <dd></dd> <dt>

<span id="128"></span>

**128** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Name by which the physical element is generally known.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Number**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Physical slot number, which can be used as an index into a system slot table, to determine whether the slot is physically occupied.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar-code data that is associated with an element, which also has an asset tag. Note that if only bar-code data is available, and is unique and able to be used as an element key, this property would be null and the bar-code data would be used as the class key in the **Tag** property.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Part number assigned by the organization that produced or manufactured the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PoweredOn**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the physical element is powered on.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PurposeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Slot**.**SpecialPurpose**")
</dt> </dl>

Free-form string that describes how this slot is physically unique and that it may hold special types of hardware. This property only has meaning when the corresponding Boolean **SpecialPurpose** property is set to **TRUE**.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Manufacturer-allocated number used to identify the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Stock-keeping unit number for the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SpecialPurpose**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Slot**.**PurposeDescription**")
</dt> </dl>

If **TRUE**, the slot is physically unique and may hold special types of hardware, (for example, a graphics processor slot). If **TRUE**, the **PurposeDescription** property should specify how the slot is unique or the slot's purpose.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportsHotPlug**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the slot supports hot-plugging of adapter cards.

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Arbitrary string that uniquely identifies the physical element and serves as the element's key. This property can contain information, such as asset tag or serial number data. The key for [**CIM\_PhysicalElement**](cim-physicalelement.md) is placed very high in the object hierarchy to independently identify the hardware/entity, regardless of physical placement in (or on) cabinets, adapters, and so on. For example, a removable component that can be hot-swapped can be taken from its containing (scoping) package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. The key for a physical element is an arbitrary string that is defined independently of placement or location-oriented hierarchy.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**ThermalRating**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Slot\|004.11"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("milliwatts")
</dt> </dl>

Maximum thermal dissipation of the slot, in milliwatts.

</dd> <dt>

**VccMixedVoltageSupport**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Slot\|004.9")
</dt> </dl>

Vcc voltage supported by the slot.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="3.3V"></span><span id="3.3v"></span>

**3.3V** (2)


</dt> <dd></dd> <dt>

<span id="5V"></span><span id="5v"></span>

**5V** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Version of the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**VppMixedVoltageSupport**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Slot\|004.10")
</dt> </dl>

Vpp voltage supported by the slot.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="3.3V"></span><span id="3.3v"></span>

**3.3V** (2)


</dt> <dd></dd> <dt>

<span id="5V"></span><span id="5v"></span>

**5V** (3)


</dt> <dd></dd> <dt>

<span id="12V"></span><span id="12v"></span>

**12V** (4)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **CIM\_Slot** class is derived from [**CIM\_PhysicalConnector**](cim-physicalconnector.md).

WMI does not implement this class. For WMI classes derived from **CIM\_Slot**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalConnector**](cim-physicalconnector.md)
</dt> </dl>

 


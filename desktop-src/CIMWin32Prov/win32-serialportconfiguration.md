---
description: The Win32\_SerialPortConfiguration WMI class represents the settings for data transmission on a Windows-based serial port. This includes configurations for establishing a connection and error checking.
ms.assetid: 688cdcce-8325-4b4d-93ab-5a602e9e3f8e
ms.tgt_platform: multiple
title: Win32_SerialPortConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SerialPortConfiguration
- Win32_SerialPortConfiguration.Caption
- Win32_SerialPortConfiguration.Description
- Win32_SerialPortConfiguration.SettingID
- Win32_SerialPortConfiguration.AbortReadWriteOnError
- Win32_SerialPortConfiguration.BaudRate
- Win32_SerialPortConfiguration.BinaryModeEnabled
- Win32_SerialPortConfiguration.BitsPerByte
- Win32_SerialPortConfiguration.ContinueXMitOnXOff
- Win32_SerialPortConfiguration.CTSOutflowControl
- Win32_SerialPortConfiguration.DiscardNULLBytes
- Win32_SerialPortConfiguration.DSROutflowControl
- Win32_SerialPortConfiguration.DSRSensitivity
- Win32_SerialPortConfiguration.DTRFlowControlType
- Win32_SerialPortConfiguration.EOFCharacter
- Win32_SerialPortConfiguration.ErrorReplaceCharacter
- Win32_SerialPortConfiguration.ErrorReplacementEnabled
- Win32_SerialPortConfiguration.EventCharacter
- Win32_SerialPortConfiguration.IsBusy
- Win32_SerialPortConfiguration.Name
- Win32_SerialPortConfiguration.Parity
- Win32_SerialPortConfiguration.ParityCheckEnabled
- Win32_SerialPortConfiguration.RTSFlowControlType
- Win32_SerialPortConfiguration.StopBits
- Win32_SerialPortConfiguration.XOffCharacter
- Win32_SerialPortConfiguration.XOffXMitThreshold
- Win32_SerialPortConfiguration.XOnCharacter
- Win32_SerialPortConfiguration.XOnXMitThreshold
- Win32_SerialPortConfiguration.XOnXOffInFlowControl
- Win32_SerialPortConfiguration.XOnXOffOutFlowControl
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SerialPortConfiguration class

The **Win32\_SerialPortConfiguration** [WMI class](../wmisdk/retrieving-a-class.md) represents the settings for data transmission on a Windows-based serial port. This includes configurations for establishing a connection and error checking.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4EB-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SerialPortConfiguration : CIM_Setting
{
  string  Caption;
  string  Description;
  string  SettingID;
  boolean AbortReadWriteOnError;
  uint32  BaudRate;
  boolean BinaryModeEnabled;
  uint32  BitsPerByte;
  boolean ContinueXMitOnXOff;
  boolean CTSOutflowControl;
  boolean DiscardNULLBytes;
  boolean DSROutflowControl;
  boolean DSRSensitivity;
  string  DTRFlowControlType;
  uint32  EOFCharacter;
  uint32  ErrorReplaceCharacter;
  boolean ErrorReplacementEnabled;
  uint32  EventCharacter;
  boolean IsBusy;
  string  Name;
  string  Parity;
  boolean ParityCheckEnabled;
  string  RTSFlowControlType;
  string  StopBits;
  uint32  XOffCharacter;
  uint32  XOffXMitThreshold;
  uint32  XOnCharacter;
  uint32  XOnXMitThreshold;
  uint32  XOnXOffInFlowControl;
  uint32  XOnXOffOutFlowControl;
};
```

## Members

The **Win32\_SerialPortConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SerialPortConfiguration** class has these properties.

<dl> <dt>

**AbortReadWriteOnError**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fAbortOnError")
</dt> </dl>

If **TRUE**, read and write operations are terminated if an error occurs. If **TRUE**, the driver terminates all read and write operations with an error status if an error occurs. The driver will not accept any further communications operations until the application acknowledges the error.

</dd> <dt>

**BaudRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|BaudRate")
</dt> </dl>

Baud (bits per second) rate at which the communications device operates.

Example: 9600

</dd> <dt>

**BinaryModeEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fBinary")
</dt> </dl>

If **TRUE**, binary-mode data transfers are enabled for the serial port. Computer systems running Windows only allow binary transfers through serial ports, so this value is always **TRUE**.

</dd> <dt>

**BitsPerByte**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|ByteSize")
</dt> </dl>

Number of bits transmitted and received for each byte of data for the Windows serial port. The number may vary with control and error correction bits, such as parity bits.

Example: 8

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**ContinueXMitOnXOff**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fTXContinueOnXoff")
</dt> </dl>

If **TRUE**, data transmissions continue when the input buffer has come within **XOffXMitThreshold** bytes of being full and the driver has transmitted the **XOffChararcter** value to stop receiving bytes. If **FALSE**, transmission does not continue until the input buffer is within **XOnXMitThreshold** bytes of being empty and the driver has transmitted the **XOnCharacter** value to resume reception.

</dd> <dt>

**CTSOutflowControl**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fOutxCtsFlow")
</dt> </dl>

If **TRUE**, the clear to send (CTS) signal is checked before transmitting data. CTS signals that both devices on the serial connection are ready to transfer data. Data transmission is suspended until the CTS signal is given.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**DiscardNULLBytes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fNull")
</dt> </dl>

If **TRUE**, **NULL** bytes (characters) are discarded when they are received.

</dd> <dt>

**DSROutflowControl**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fOutxDsrFlow")
</dt> </dl>

If **TRUE**, data outflow control is enabled when there is a data set ready (DSR) condition. DSR signals that the connection has been established by the devices on the serial connection. DSR data transmission is suspended until the DSR signal is given.

</dd> <dt>

**DSRSensitivity**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fDsrSensitivity")
</dt> </dl>

If **TRUE**, the communications driver is sensitive to the state of the DSR signal. The driver ignores any bytes received, unless the DSR modem input line is high.

</dd> <dt>

**DTRFlowControlType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fDtrControl")
</dt> </dl>

Use of the data terminal ready (DTR) flow control after a connection has been established.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** ("Enable")


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> <dt>

<span id="Handshake"></span><span id="handshake"></span><span id="HANDSHAKE"></span>

**Handshake** ("Handshake")


</dt> <dd></dd> </dl>

</dd> <dt>

**EOFCharacter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|EofChar")
</dt> </dl>

Value of the character used to signal the end of data.

Example: ^Z

</dd> <dt>

**ErrorReplaceCharacter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|ErrorChar")
</dt> </dl>

Value of the character used to replace bytes received with a parity error.

Example: ^C

</dd> <dt>

**ErrorReplacementEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fErrorChar")
</dt> </dl>

If **TRUE**, bytes received with parity errors are replaced with the **ErrorReplaceCharacter** value. Characters with parity errors are only replaced if this property is **TRUE** and the parity is enabled.

</dd> <dt>

**EventCharacter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|EvtChar")
</dt> </dl>

Value of the control character that is used to signal an event, such as end of file.

Example: ^e

</dd> <dt>

**IsBusy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|File Functions\|CreateFile")
</dt> </dl>

If **TRUE**, the serial port is busy.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Hardware\\\\DeviceMap\\\\SerialComm")
</dt> </dl>

Name of the Windows serial port.

Example: "COM1"

</dd> <dt>

**Parity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|Parity")
</dt> </dl>

Method of parity checking to be used. Parity is used as an error checking technique where an extra parity bit is included with every unit of data. The receiver can then verify the validity of the data by counting the bits that are set.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** ("None")


</dt> <dd>

Parity checking not used.

</dd> <dt>

<span id="Odd"></span><span id="odd"></span><span id="ODD"></span>

<span id="Odd"></span><span id="odd"></span><span id="ODD"></span>**Odd** ("Odd")


</dt> <dd>

Sets the parity bit so that the count of bits set is an odd number.

</dd> <dt>

<span id="Even"></span><span id="even"></span><span id="EVEN"></span>

<span id="Even"></span><span id="even"></span><span id="EVEN"></span>**Even** ("Even")


</dt> <dd>

Sets the parity bit so that the count of bits set is an even number.

</dd> <dt>

<span id="Mark"></span><span id="mark"></span><span id="MARK"></span>

<span id="Mark"></span><span id="mark"></span><span id="MARK"></span>**Mark** ("Mark")


</dt> <dd>

Leaves the parity bit set to 1.

</dd> <dt>

<span id="Space"></span><span id="space"></span><span id="SPACE"></span>

<span id="Space"></span><span id="space"></span><span id="SPACE"></span>**Space** ("Space")


</dt> <dd>

Leaves the parity bit set to 0 (zero).

</dd> </dl>

</dd> <dt>

**ParityCheckEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fParity")
</dt> </dl>

If **TRUE**, parity checking is enabled.

</dd> <dt>

**RTSFlowControlType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Request to send (RTS) flow control. RTS is used to signal that data is available for transmission.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>**Enable** ("Enable")


</dt> <dd>

RTS is left on for the data transfer session.

</dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>**Disable** ("Disable")


</dt> <dd>

RTS is ignored after the first RTS signal is received.

</dd> <dt>

<span id="Handshake"></span><span id="handshake"></span><span id="HANDSHAKE"></span>

<span id="Handshake"></span><span id="handshake"></span><span id="HANDSHAKE"></span>**Handshake** ("Handshake")


</dt> <dd>

RTS is turned off if the transmission buffer is more than three-quarters full, and RTS is turned on when the buffer is less than one-half full.

</dd> <dt>

<span id="Toggle"></span><span id="toggle"></span><span id="TOGGLE"></span>

<span id="Toggle"></span><span id="toggle"></span><span id="TOGGLE"></span>**Toggle** ("Toggle")


</dt> <dd>

RTS is turned on if there is any data buffered for transmission.

</dd> </dl>

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**StopBits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|StopBits")
</dt> </dl>

Number of stop bits to be used. Stop bits separate each unit of data on an asynchronous serial connection. They are also sent continuously when no data is available for transmission.

<dt>

<span id="1"></span>

**1** ("1")


</dt> <dd></dd> <dt>

<span id="1.5"></span>

**1.5** ("1.5")


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** ("2")


</dt> <dd></dd> </dl>

</dd> <dt>

**XOffCharacter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|XoffChar")
</dt> </dl>

Value of the XOFF character for both transmission and reception. XOFF is a software control to stop the transmission of data (whereas RTS and CTS are hardware controls). XON resumes the transmission.

</dd> <dt>

**XOffXMitThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|XoffLim")
</dt> </dl>

Maximum number of bytes allowed in the input buffer before the XOFF character is sent.

</dd> <dt>

**XOnCharacter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|XonChar")
</dt> </dl>

Value of the XON character for both transmission and reception. XON is a software control to resume the transmission of data (whereas RTS and CTS are hardware controls). XOFF stops the transmission.

</dd> <dt>

**XOnXMitThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|XonLim")
</dt> </dl>

Minimum number of bytes allowed in the input buffer before the XON character is sent. This property works in conjunction with **XOffXMitThreshold** to regulate the rate at which data is transferred.

</dd> <dt>

**XOnXOffInFlowControl**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fInX")
</dt> </dl>

If **TRUE**, XON/XOFF flow control is used during reception. If **TRUE**, the **XOffCharacter** value is sent when the input buffer comes within **XOffXMitThreshold** bytes of being full, and the **XOnCharacter** value is sent when the input buffer comes within **XOnXMitThreshold** bytes of being empty.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

FALSE

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

TRUE

</dd> </dl>

</dd> <dt>

**XOnXOffOutFlowControl**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Communication Structures\|[**DCB**](/windows/win32/api/winbase/ns-winbase-dcb)\|fOutX")
</dt> </dl>

The **XOnXOffOutFlowControl** specifies whether XON or XOFF flow control is used during transmission. If **TRUE**, transmission stops when the **XOffCharacter** value is received and starts again when the **XOnCharacter** value is received.

</dd> </dl>

## Remarks

The **Win32\_SerialPortConfiguration** class is derived from [**CIM\_Setting**](cim-setting.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 

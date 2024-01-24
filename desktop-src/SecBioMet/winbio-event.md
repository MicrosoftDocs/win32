---
title: WINBIO_EVENT structure (Winbio\_types.h)
description: Contains status information sent to the callback routine when an event notice is raised.
ms.assetid: f46df7ff-8197-49cb-b1f8-4e7e3288e3df
keywords:
- WINBIO_EVENT structure Windows Biometric Framework API
- PWINBIO_EVENT structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_EVENT
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_EVENT structure

The **WINBIO\_EVENT** structure contains status information sent to the callback routine when an event notice is raised.

## Syntax


```C++
typedef struct _WINBIO_EVENT {
  WINBIO_EVENT_TYPE Type;
  union {
    struct {
      WINBIO_UNIT_ID       UnitId;
      WINBIO_REJECT_DETAIL RejectDetail;
    } Unclaimed;
    struct {
      WINBIO_UNIT_ID           UnitId;
      WINBIO_IDENTITY          Identity;
      WINBIO_BIOMETRIC_SUBTYPE SubFactor;
      WINBIO_REJECT_DETAIL     RejectDetail;
    } UnclaimedIdentify;
    struct {
      HRESULT ErrorCode;
    } Error;
  } Parameters;
} WINBIO_EVENT, *PWINBIO_EVENT;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

A value that specifies the type of service provider event notice raised. The only provider currently supported is the fingerprint sensor. This sensor supports the following flags.

<dl> <dt>

<span id="WINBIO_EVENT_FP_UNCLAIMED"></span><span id="winbio_event_fp_unclaimed"></span>**WINBIO\_EVENT\_FP\_UNCLAIMED** (The sensor detected a finger swipe that was not requested by the application or by the window that currently has focus. The Windows Biometric Framework calls into your callback function to indicate that a finger swipe has occurred but does not try to identify the fingerprint.)
</dt> <dt>

<span id="WINBIO_EVENT_FP_UNCLAIMED_IDENTIFY"></span><span id="winbio_event_fp_unclaimed_identify"></span>**WINBIO\_EVENT\_FP\_UNCLAIMED\_IDENTIFY** (The sensor detected a finger swipe that was not requested by the application or by the window that currently has focus. The Windows Biometric Framework attempts to identify the fingerprint and passes the result of that process to your callback function.)
</dt> </dl> </dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

**Unclaimed**
</dt> <dd>

Structure returned for biometric sample capture.

<dl> <dt>

**UnitId**
</dt> <dd>

The biometric unit that generated the sample.

</dd> <dt>

**RejectDetail**
</dt> <dd>

A **ULONG** value that contains additional information regarding failure to capture a biometric sample. If a capture succeeded, this parameter is set to zero. The following values are defined for fingerprint capture:

-   WINBIO\_FP\_TOO\_HIGH
-   WINBIO\_FP\_TOO\_LOW
-   WINBIO\_FP\_TOO\_LEFT
-   WINBIO\_FP\_TOO\_RIGHT
-   WINBIO\_FP\_TOO\_FAST
-   WINBIO\_FP\_TOO\_SLOW
-   WINBIO\_FP\_POOR\_QUALITY
-   WINBIO\_FP\_TOO\_SKEWED
-   WINBIO\_FP\_TOO\_SHORT
-   WINBIO\_FP\_MERGE\_FAILURE

</dd> </dl> </dd> <dt>

**UnclaimedIdentify**
</dt> <dd>

Structure returned for biometric capture and identification. Identification determines whether a sample can be associated with an existing biometric template.

<dl> <dt>

**UnitId**
</dt> <dd>

The biometric unit that generated the sample.

</dd> <dt>

**Identity**
</dt> <dd>

A [**WINBIO\_IDENTITY**](winbio-identity.md) structure that contains the GUID or SID of the user providing the biometric sample.

</dd> <dt>

**SubFactor**
</dt> <dd>

A [**WINBIO\_BIOMETRIC\_SUBTYPE**](winbio-biometric-subtype-constants.md) value that specifies the sub-factor associated with a biometric sample. The Windows Biometric Framework (WBF) currently supports only fingerprint capture and uses the following constants to represent sub-type information.

-   WINBIO\_ANSI\_381\_POS\_UNKNOWN
-   WINBIO\_ANSI\_381\_POS\_RH\_THUMB
-   WINBIO\_ANSI\_381\_POS\_RH\_INDEX\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_MIDDLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_RING\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_LITTLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_THUMB
-   WINBIO\_ANSI\_381\_POS\_LH\_INDEX\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_MIDDLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_RING\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_LITTLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_FOUR\_FINGERS
-   WINBIO\_ANSI\_381\_POS\_LH\_FOUR\_FINGERS
-   WINBIO\_ANSI\_381\_POS\_TWO\_THUMBS

> [!IMPORTANT]
>
> Do not attempt to validate the value supplied for the *SubFactor* value. The Windows Biometrics Service will validate the supplied value before passing it through to your implementation. If the value is **WINBIO\_SUBTYPE\_NO\_INFORMATION** or **WINBIO\_SUBTYPE\_ANY**, then validate where appropriate.

 

</dd> <dt>

**RejectDetail**
</dt> <dd>

A **ULONG** value that contains additional information about the failure to capture a biometric sample. If the capture succeeded, this parameter is set to zero. The following values are defined for fingerprint capture:

-   WINBIO\_FP\_TOO\_HIGH
-   WINBIO\_FP\_TOO\_LOW
-   WINBIO\_FP\_TOO\_LEFT
-   WINBIO\_FP\_TOO\_RIGHT
-   WINBIO\_FP\_TOO\_FAST
-   WINBIO\_FP\_TOO\_SLOW
-   WINBIO\_FP\_POOR\_QUALITY
-   WINBIO\_FP\_TOO\_SKEWED
-   WINBIO\_FP\_TOO\_SHORT
-   WINBIO\_FP\_MERGE\_FAILURE

</dd> </dl> </dd> <dt>

**Error**
</dt> <dd>

Structure that identifies the success or failure of the operation being monitored.

<dl> <dt>

**ErrorCode**
</dt> <dd>

**HRESULT** value that contains S\_OK or an error code that resulted from computations performed by the Windows Biometric Framework.

</dd> </dl> </dd> </dl> </dd> </dl>

## Remarks

Call the [**WinBioRegisterEventMonitor**](/windows/desktop/api/Winbio/nf-winbio-winbioregistereventmonitor) function to register a callback routine to receive event notifications from the Windows Biometric Framework. The callback is a custom function that you must define for your application.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> <dt>

[**WinBioRegisterEventMonitor**](/windows/desktop/api/Winbio/nf-winbio-winbioregistereventmonitor)
</dt> </dl>

 

 






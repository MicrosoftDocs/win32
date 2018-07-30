---
Description: The transfer operation allows an application to send a currently connected communications session to a different address.
ms.assetid: b1027f09-74e1-4da8-b718-bb55a56dda1d
title: Transfer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Transfer

The transfer operation allows an application to send a currently connected communications session to a different address.

TAPI provides two mechanisms for transferring a current session to a different address. *Blind transfer* allows an existing session to be transferred to a specified destination address in one phase. *Consultation transfer* requires the existence of a consultation session in addition to the current session to set up for the transfer, and then completion of the transfer. The choice between these two types is frequently based on service provider capabilities because some service providers do not support blind transfer. In some cases, application needs may make the consultative transfer the preferred method even where blind transfer is possible.

The blind transfer operation is basically the same under TAPI 2 and TAPI 3, but consultative transfer follows slightly different patterns.

**TAPI 2.x:** Consultative transfer starts with invoking [**lineSetupTransfer**](https://msdn.microsoft.com/en-us/library/ms736115(v=VS.85).aspx), which places the existing call on consultation hold, and identifies this call as the target for the next transfer-completion request. The **lineSetupTransfer** function also allocates a consultation call that can be used to establish the consultation call with the party to which the call will be transferred. The application can dial the extension of the destination party on the consultation call (using [**lineDial**](https://msdn.microsoft.com/en-us/library/ms735612(v=VS.85).aspx)), or it can drop and deallocate the consultation call and instead activate an existing held call (using [**lineUnhold**](https://msdn.microsoft.com/en-us/library/ms736477(v=VS.85).aspx)), if supported by the switch. While the initial call is on consultation hold and the consultation call is active, the application can toggle between these calls using [**lineSwapHold**](https://msdn.microsoft.com/en-us/library/ms736121(v=VS.85).aspx).

**TAPI 2.x:** Applications complete the consultative transfer using [**lineCompleteTransfer**](https://msdn.microsoft.com/en-us/library/ms735578(v=VS.85).aspx). Both calls will revert to the *idle* state.

Applications can use the "one-step transfer" feature of many PBXs (a single button press to establish a consultation transfer) by setting the *lpCallParams* parameter to the **LINECALLPARAMFLAGS\_ONESTEPTRANSFER** member of the [LINECALLPARAMFLAGS\_ constants](https://msdn.microsoft.com/en-us/library/ms735533(v=VS.85).aspx) when calling [**lineSetupTransfer**](https://msdn.microsoft.com/en-us/library/ms736115(v=VS.85).aspx).

**TAPI 3.x:** Consultative transfer starts with using [**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall) to create a consultation call to the new destination address. [**ITBasicCallControl::Transfer**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-transfer) is then called on the original call object using a pointer to the new consultation call object as a parameter. Calling [**ITBasicCallControl::Finish**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-finish) on the consultation call object then completes the transfer.

The application must release session resources following the successful completion of a transfer operation.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineBlindTransfer**](https://msdn.microsoft.com/en-us/library/ms735509(v=VS.85).aspx), [**lineSetupTransfer**](https://msdn.microsoft.com/en-us/library/ms736115(v=VS.85).aspx), [**lineCompleteTransfer**](https://msdn.microsoft.com/en-us/library/ms735578(v=VS.85).aspx).

**TAPI 3.x:** See [**ITBasicCallControl::BlindTransfer**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-blindtransfer), [**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall), [**ITBasicCallControl::Transfer**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-transfer), [**ITBasicCallControl::Finish**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-finish).

 

 




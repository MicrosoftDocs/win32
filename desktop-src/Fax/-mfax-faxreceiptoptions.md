---
Description: 'The FaxReceiptOptions configuration object is used by a fax client application to set and retrieve the receipt configuration that the fax service uses to send delivery receipts for fax transmissions.'
ms.assetid: '6c3d1358-6819-42e3-9be0-896ed7e2d463'
title: FaxReceiptOptions object
---

# FaxReceiptOptions object

The **FaxReceiptOptions** configuration object is used by a fax client application to set and retrieve the receipt configuration that the fax service uses to send delivery receipts for fax transmissions.

## Members

The **FaxReceiptOptions** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxReceiptOptions** object has these methods.



| Method                                                | Description                                                                                                                                                                                                                                                                                                    |
|:------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-faxreceiptoptions-refresh-vb.md) | The [**Refresh**](-mfax-faxreceiptoptions-refresh-vb.md) method refreshes **FaxReceiptOptions** object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxreceiptoptions-save-vb.md) method call are lost.<br/> |
| [**Save**](-mfax-faxreceiptoptions-save-vb.md)       | The [**Save**](-mfax-faxreceiptoptions-save-vb.md) method saves the **FaxReceiptOptions** object data.<br/>                                                                                                                                                                                             |



 

### Properties

The **FaxReceiptOptions** object has these properties.



| Property                                                                                   | Access type           | Description                                                                                                                                                                                                                                                                    |
|:-------------------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllowedReceipts**](-mfax-faxreceiptoptions-allowedreceipts-vb.md)<br/>           | Read/write<br/> | The [**AllowedReceipts**](-mfax-faxreceiptoptions-allowedreceipts-vb.md) property is a value that specifies the permitted types of delivery receipts.<br/>                                                                                                              |
| [**AuthenticationType**](-mfax-faxreceiptoptions-authenticationtype-vb.md)<br/>     | Read/write<br/> | The [**AuthenticationType**](-mfax-faxreceiptoptions-authenticationtype-vb.md) property specifies the type of authentication the fax service uses when connecting to an SMTP server. <br/>                                                                              |
| [**SMTPPassword**](-mfax-faxreceiptoptions-smtppassword-vb.md)<br/>                 | Read/write<br/> | The [**SMTPPassword**](-mfax-faxreceiptoptions-smtppassword-vb.md) property is a null-terminated string that contains the SMTP password used for authenticated connections.<br/>                                                                                        |
| [**SMTPPort**](-mfax-faxreceiptoptions-smtpport-vb.md)<br/>                         | Read/write<br/> | The [**SMTPPort**](-mfax-faxreceiptoptions-smtpport-vb.md) property is a value that specifies the SMTP port number.<br/>                                                                                                                                                |
| [**SMTPSender**](-mfax-faxreceiptoptions-smtpsender-vb.md)<br/>                     | Read/write<br/> | The [**SMTPSender**](-mfax-faxreceiptoptions-smtpsender-vb.md) property is a null-terminated string that contains the SMTP email address for the sender of the mail message receipt.<br/>                                                                               |
| [**SMTPServer**](-mfax-faxreceiptoptions-smtpserver-vb.md)<br/>                     | Read/write<br/> | The [**SMTPServer**](-mfax-faxreceiptoptions-smtpserver-vb.md) property is a null-terminated string that contains the name of the SMTP server.<br/>                                                                                                                     |
| [**SMTPUser**](-mfax-faxreceiptoptions-smtpuser-vb.md)<br/>                         | Read/write<br/> | The [**SMTPUser**](-mfax-faxreceiptoptions-smtpuser-vb.md) property is a null-terminated string that contains the SMTP user name used for authenticated connections. <br/>                                                                                              |
| [**UseForInboundRouting**](-mfax-faxreceiptoptions-useforinboundrouting-vb.md)<br/> | Read/write<br/> | The [**UseForInboundRouting**](-mfax-faxreceiptoptions-useforinboundrouting-vb.md) property sets or retrieves whether to use the **FaxReceiptOptions** settings for the Microsoft Routing Extension, which allows incoming faxes to be routed to email addresses. <br/> |



 

## Remarks

A **FaxReceiptOptions** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object.

![faxserver and faxreceiptoptions objects](images/faxreceiptoptions.png)

> [!Note]  
> Changes made to the **FaxReceiptOptions** object will not be saved until you call the [**Save**](-mfax-faxreceiptoptions-save-vb.md) method.

 

To create a **FaxReceiptOptions** object in Microsoft Visual Basic, call the [**ReceiptOptions**](-mfax-faxserver-receiptoptions.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

To create a **FaxReceiptOptions** object in C++, call the [**ReceiptOptions**](-mfax-faxserver-receiptoptions.md) method.

You can configure the fax service to send delivery receipts for fax transmissions. If you choose to send delivery receipts, there are receipt options that you should set. You should select the type of receipt, such as a message box or email message. If you select to send an email message, there are a number of properties that you have to set, specific to that type of receipt. You set these receipt options using the **FaxReceiptOptions** configuration object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxReceiptOptions<br/>                                                     |



## See also

<dl> <dt>

[**IFaxReceiptOptions**](-mfax-faxreceiptoptions-cpp.md)
</dt> </dl>

 

 





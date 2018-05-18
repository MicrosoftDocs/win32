---
Description: 'Frequently asked questions for Web Authentication Broker.'
ms.assetid: '49ACB2E3-CF57-4D8E-9670-E7C18A06F76A'
title: FAQ for Web Authentication Broker
---

# FAQ for Web Authentication Broker

Frequently asked questions for Web Authentication Broker.



| Question                                                                                                    | Answer                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| How can I make sure that my https:// page works with the Web Authentication Broker?                         | Try loading the page in Windows Internet Explorer before trying it with Web Authentication Broker. If your web page loads with no errors, it will be rendered correctly by the Web Authentication Broker as well. |
| In case of an error, will the error codes be displayed to the user?                                         | While an error page will be displayed to the user, the underlying error code is not shown. It is only returned to the app. Alternately, you can also use the operational logs.                                    |
| How can I find more details on the error encountered?                                                       | Use the operational logs for details.                                                                                                                                                                             |
| Does the single sign-on (SSO) app container share its cookies with the Internet Explorer or other browsers? | No.                                                                                                                                                                                                               |



 

## Related topics

<dl> <dt>

[Considerations for the web page development](considerations-for-the-web-page-development.md)
</dt> <dt>

[Web Authentication Broker SDK sample app](http://code.msdn.microsoft.com/windowsapps/Web-Authentication-d0485122#content)
</dt> <dt>

[**Windows.Security.Authentication.Web**](https://msdn.microsoft.com/library/windows/apps/br227044)
</dt> </dl>

 

 




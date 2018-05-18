---
title: Deploy into production
description: This topic guides you through deployment options for your rights-enabled application.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '4B785564-6839-49ED-A243-E2A6DFF88B2E'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Deploy into production

This topic guides you through deployment options for your rights-enabled application.

## Request a Production License Agreement

Before you can release an application developed using the Rights Management Services SDK 2.1, you must apply for a Production License Agreement to obtain a production certificate.

> \[!Important\]
>
> If you will be running your client application with Azure based RMS, you'll need to create your own tenants. For more information, see [Azure RMS requirements: Cloud subscriptions that support Azure RMS](https://docs.microsoft.com/rights-management/get-started/requirements-subscriptions)
>
> For more information on running with Azure RMS see, [Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md).

 

You can obtain the certificate by applying for a Production License Agreement.

-   Send an email message to [RMLA@microsoft.com](mailto:rmla@microsoft.com) and include the following information:

    -   Full company name
    -   Physical corporate address (include the city, state, country or region, and zip or postal code)
    -   Corporate mailing address (include the city, state, country or region, and zip or postal code)
    -   Company phone and fax numbers
    -   Company URL
    -   Country or region of incorporation
    -   Application or product name
    -   First and last name of the requester
    -   Title or position of the requester
    -   Email address of the requester

    Although an email account is not strictly required, the application process typically relies on email for communication. You can get a free email account at Microsoft Outlook.com. If you do not have an account and do not want one, you can send a typewritten application to the following address:

    `Active Directory Rights Management License Agreements (ADRMLA)`

    `Microsoft Corporation`

    `One Microsoft Way`

    `Redmond, WA 98052-6399`

    When requesting an agreement, please do the following;

    -   Submit the information, in English, as it should appear on the agreement.
    -   Send all requested information. Missing or incomplete information can delay processing of your request.

    The Active Directory Rights Management Licensing Agreement (ADRMLA) team will respond to your emailed request within three business days, longer if you sent the request by using a postal service. The response will include the license agreement form and further instructions. Read, sign, and return all pages of the agreement to the ADRMLA team. Please do not change the fonts or reformat the paragraphs of the license agreement.

    Be sure to follow the instructions you receive from the ADRMLA team. The instructions list the items of digital information needed to fulfill your certificate request. By following the step-by-step instructions you will reduce delays.

    The ADRMLA team will forward your production certificate to you after it is created. Please note that it may take up to 15 business days for the ADRMLA team to reply with your certificate by email, longer if communication is by postal service.

## Installation options and requirements for Rights Management Service Client 2.1

Given that you utilized RMS SDK 2.1, you will need Rights Management Service Client 2.1 to be deployed on the end-user machine.

**RMS Client 2.1**

The RMS Client 2.1 is software designed for your client computers to help protect access to and usage of information flowing through applications that use RMS whether installed on your premises or in a Microsoft datacenter.

The RMS Client 2.1 is not a Windows operating system component. The RMS Client 2.1 ships as an optional download which can be, with acknowledgment and acceptance of its license agreement, freely distributed with your third-party software to enable client access content that has been rights protected by use and deployment of RMS servers in your environment.

> \[!Important\]  
> The RMS Client 2.1 is architecture specific and must match the architecture of your target operating system.

 

**RMS Client 2.1 installation choices**

-   **Redistributing the RMS Client 2.1**

    The recommended approach is to bundle RMS Client installer package with your application or solution using your preferred installation technology. The RMS Client can be freely redistributed and bundled with other applications and IT solutions.

    You can choose to install the RMS Client 2.1 interactively by starting the RMS Client 2.1 installer or silently install it. The integration steps will be:

    -   Download RMS Client 2.1 installer
    -   Integrate the RMS Client 2.1 installer run with your application installer

    Two good examples of integrating the RMS Client 2.1 with your application are the RMS SDK 2.1 installer package and the Right Protected Folder Explorer package. Try installing them yourself to understand the approach.

-   **Make RMS Client 2.1 a pre-requisite for your application install**

    In this case, you will create a pre-requisite such that your application install will fail if RMS Client 2.1 is not present on the end-user machine.

    If the client is not present, provide an error message informing the user where they can download a copy of the RMS Client 2.1

    If the client is present, proceed with your application installation.

**Enabling Azure Rights Management Services with your application**

> [!Note]
>
> If you have migrated to the new ADAL model for authentication, you don’t have to install SIA. For more information, see [ADAL authentication for your RMS enabled application](authentication-with-adal.md).
>
> Also, you can **Certify your application for Windows 10** - By updating your application to use ADAL authentication rather than the Microsoft Online Sign-in Assistant, you and your customers will be able to:
>
> <dl> Utilize multi-factor authentication  
> Install the RMS Client 2.1 without requiring administrative privileges to the machine  
> </dl>

 

In order for your end-user to take advantage of Azure Rights Management services, you must deploy the *Online Services Sign-in Assistant (SIA)*. As the application developer, you do not know whether the end-user will use RMS (on premises) or Azure Rights Management services (cloud service).

> \[!Important\]  
> Running your RMS SDK 2.1 client application with Azure RMS, requires you to create your own tenants. For more information, see [Azure RMS requirements: Cloud subscriptions that support Azure RMS](https://docs.microsoft.com/rights-management/get-started/requirements-subscriptions)

 

-   Download the [Microsoft Online Services Sign-In Assistant](http://www.microsoft.com/download/details.aspx?id=28177) from the Microsoft Download Center.
-   Ensure that your deployment of a rights-enabled application includes a pre-requisites check for this service selection.
-   For your own testing and for your end-users use of the on-line service see the TechNet topic, [Configuring Rights Management](https://TechNet.Microsoft.Com/library/jj585002.aspx).

For more on enabling your application to use RMS for Azure Rights Management services see, [Enable your application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md).

## Related topics

<dl> <dt>

[How-to use](https://msdn.microsoft.com/library/windows/desktop/hh535252)
</dt> <dt>

[Microsoft Online Services Sign-In Assistant](http://www.microsoft.com/download/details.aspx?id=28177)
</dt> <dt>

[Configuring Rights Management](https://TechNet.Microsoft.Com/library/jj585002.aspx)
</dt> <dt>

[Enable your application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md)
</dt> </dl>

 

 





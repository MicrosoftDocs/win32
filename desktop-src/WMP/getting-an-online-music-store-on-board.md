---
title: Getting an Online Music Store On Board
description: Getting an Online Music Store On Board
ms.assetid: f7eff687-9832-41bc-8f3d-a2ab11917eb0
keywords:
- Windows Media Player Online Stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Getting an Online Music Store On Board

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes the process of bringing an online digital media store on board for Windows Media Player. The time required for the on-boarding process from start to finish is approximately 45-60 BUSINESS DAYS. The two stages of the on-boarding process are described in the following table.




| Stage | Description | 
|-------|-------------|
| Pending | <ul><li>You send Microsoft the required contact information, startup information, and validation accounts.</li><li>Microsoft sends you a test key and a production key.</li><li>You test your online store with Windows Media Player.</li><li>You submit signed agreements and contracts to Microsoft.</li></ul> | 
| Validation | Microsoft validates your online store. | 




 

After you complete the pending and validation stages, Microsoft will publish your online store.

## Pending Stage

The pending stage gives you an opportunity to test your online store in Windows Media Player. It is also a good time to make sure that all required agreements and contracts are signed. To get started, send Microsoft the following information, as defined later in this topic:

-   Contact information
-   Startup information
-   Validation accounts

Upon receipt of your contact and startup information, Microsoft will send you a test key and a production key. After you have added your test key to the registry and restarted the Player, your online store will appear in the Player, and you will be able to test it. For information about where to put your test key in the registry, see [Registry Keys and Entries for a Type 1 Online Store](registry-keys-and-entries-for-a-type-1-online-store.md) or [Registry Keys and Entries for a Type 2 Online Store](registry-keys-and-entries-for-a-type-2-online-store.md).

You should test all aspects of your online store, including its user interface and its plug-in. As part of your testing process, you must run the tests described in [Validation Tests for Type 2 Online Music Stores](validation-tests-for-type-2-online-music-stores.md).

> [!Note]  
> Type 1 stores must pass all of the validation tests for type 2 stores plus some additional tests that are specific to the type 1 experience. For information about type 1 validation tests, contact the Windows Media Player Services Virtual Team at mpsvctm@microsoft.com.

 

## Contact Information

The following table shows the contact information that Microsoft requires for your online store. Fill out the [Contact Information form](contact-information-form-for-an-online-music-store.md) and send it to the Windows Media Player Services Virtual Team at mpsvctm@microsoft.com.



| Item                     | Description                                                                               |
|--------------------------|-------------------------------------------------------------------------------------------|
| Store Name               | The branded name of your store                                                            |
| Provider Name            | The name of the provider/white label company (if different)                               |
| Store Locale             | The Windows User Locale(s) your store must be displayed in                                |
| Store Category           | Music, Radio, Film, TV, Sports, News, Audio Entertainment, and/or Other (please describe) |
| Purchase Model           | Purchase, Rental, Subscription, and/or Other (please describe)                            |
| Store Language           |                                                                                           |
| Store Contact Name(s)    |                                                                                           |
| Store Contact E-mail(s)  |                                                                                           |
| MSFT Passport Account(s) | This is for possible future nominations in beta and partner development programs.         |
| Shipping Address         | No P.O. Boxes                                                                             |
| City                     |                                                                                           |
| State                    |                                                                                           |
| Postal Code              |                                                                                           |
| Country/Region           |                                                                                           |
| Telephone                |                                                                                           |
| Fax                      |                                                                                           |
| Survey Contact           | Is it okay if we contact you about your experience with the program in the future?        |



 

## Startup Information

For each geographic region that your store will serve, send Microsoft a set of startup information for your test store, a set of startup information for your production store, and a set of validation accounts.

The topic [Startup Information Form for an Online Music Store](startup-information-form-for-an-online-music-store.md) contains two copies of the Startup Information form and one copy of the Validation Accounts form. Fill out the forms and send them to the Windows Media Player Services Virtual Team at mpsvctm@microsoft.com.

The following table describes the startup information that Microsoft requires for your online store.



| Item                                                                                                     | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service Info XML URL (2048-character limit)                                                              | The URL where Windows Media Player obtains your [ServiceInfo XML document](serviceinfo-document.md).                                                                                                                                         |
| Service Key (Unique ID)                                                                                  | A string that uniquely identifies your online store. You should create one for production and one for testing (for example, "MyStore" and "MyStoreTest"). Note that a service key is not the same thing as a test key.                        |
| Friendly Name (30-character limit)                                                                       | The name of your store that is displayed in the Windows Media Player service selector.                                                                                                                                                        |
| Menu Image URL (2048-character limit)                                                                    | The URL where Windows Media Player retrieves the 15 x 15 pixel logo that it displays in the service selector.                                                                                                                                 |
| Buy Music URL (2048-character limit)<br/> (Integrated music stores only)<br/>                | The URL that is used by the Player's "Buy CD" and "Shop for Music Online" links.                                                                                                                                                              |
| 10 ft UI Buy URL (2048-character limit)<br/> (Integrated music stores only -- Optional)<br/> | The URL that is used by the Player's "Buy CD" and "Shop for Music Online" links in Windows XP Media Center Edition and in Windows Media Center in Windows Vista.                                                                              |
| Store Logo (130w x 30h)<br/> (Attach PNG file separately.)<br/>                              | The store logo that is displayed in the tooltip that appears when the mouse is over the browse-all image. This logo must be a PNG-formatted file and preferably alpha-blended so that it can adjust to color changes in Windows Media Player. |
| Browse-all Image (108w x 108h)<br/> (Attach PNG file separately.)<br/>                       | The brief description in the tooltip that appears when the mouse is over your browse-all image.                                                                                                                                               |
| Store description text (110-character limit)                                                             | The text that appears in the tooltip below the store description text.                                                                                                                                                                        |
| Text for hyperlink (45-character limit)                                                                  | The store logo that is displayed on the Browse all Online Stores page. It must be a PNG-formatted file and preferably alpha-blended so that it can adjust to color changes in Windows Media Player.                                           |



 

> [!Note]  
> The 108 x 108 pixel browse-all image is a requirement for Windows Media Player 11 and later.

 

> [!Note]  
> In Windows Media Player 11 and later, the ServiceTask2 and ServiceTask3 elements of the ServiceInfo XML document are ignored. For detailed information about the ServiceInfo XML document, see [ServiceInfo Document](serviceinfo-document.md).

 

## Validation Accounts

To complete the validation process outlined in the Validation Stage section that follows, Microsoft requires five (5) validation accounts for each type of account that your online store offers. For example, if you offer accounts that differentiate between features and functionality, such as basic and premium, Microsoft will need five (5) validation accounts for each type, for a total of ten (10) accounts.

Send the user name and password for each validation account to mpsvctm@microsoft.com. Also include the name of a person that Microsoft can contact regarding validation accounts. These accounts will be used for ongoing monthly validation, so please include a process for "recharging" the accounts. One of the most common problems occurs when an online store fails to provide sufficient purchase credit for Microsoft to validate all of the purchasing scenarios. The accounts must remain active after the on-boarding process is completed.

## Validation Stage

During the validation stage, Microsoft verifies that the primary features of your online store work correctly. For all stores (type 1 and type 2), Microsoft runs the verification tests that are detailed in [Validation Tests for Type 2 Online Music Stores](validation-tests-for-type-2-online-music-stores.md). Microsoft also runs some additional validation tests for type 1 stores. If you have questions about the validation stage for type 1 stores, send mail to mpsvctm@microsoft.com.

During the validation stage, Microsoft makes two validation passes. The first pass applies to Release Candidate 1 (RC1) of your online store. If your store passes the RC1 validation, you should lock it down and make no further changes. Microsoft will do a second validation pass on your store even if your store passes the RC1 validation.

If your store fails any portion of the RC1 validation pass, you will have two weeks to create a second release candidate (RC2), which Microsoft will validate during the RC2 validation pass.

If your store fails any portion of the RC2 validation, you must wait until the following launch.

## Test and Production Keys

Recall that, during the pending stage, you sent Microsoft two sets of startup information: one for your test store and one for your production store. Also recall that Microsoft sent you two keys: a test key and a production key.

The test key is entirely for your own use. When your test key is in the registry, Windows Media Player uses the ServiceInfo URL that you submitted for your test store.

When your production key is in the registry, Windows Media Player uses the ServiceInfo URL that you submitted for your production store. Microsoft uses your production key during the validation stage. Microsoft never uses your test key for validation.

When your store is live, Windows Media Player uses the ServiceInfo URL that you submitted for your production store.

As a general rule, your test store should be the place where you develop your service and make daily changes. Your production store should be the place where you keep a stable release of your service.

## Common On-Boarding Problems

Here are some common problems that can cause your store to fail validation testing.

-   Failure to transition from test servers to production servers. This leads to many problems such as missing pages, invalid IIS and security settings, and test accounts that no longer work.
-   The Buy link (or Shop link) in the Now Playing area is invalid. This can cause your store to fail validation even when everything else is working.
-   Microsoft's validation team will test several purchasing scenarios ranging from small purchases to very large purchases. You must provide a rechargeable way for them to act as a consumer within your store. Your store can not be validated if the validation team does not have enough purchase credits to validate all of these scenarios.

For a more complete list of common on-boarding problems and frequently asked questions compiled by the Windows Media Player Services Virtual Team, see [Common On-Boarding Problems for Online Music Stores](common-on-boarding-problems-for-online-music-stores.md).

## Related topics

<dl> <dt>

[Online Stores Welcome Kit](online-stores-welcome-kit.md)
</dt> </dl>

 

 






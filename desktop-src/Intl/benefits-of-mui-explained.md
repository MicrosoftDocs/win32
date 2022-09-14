---
description: Benefits of MUI Explained
ms.assetid: 5b9851e0-4354-4088-b099-0f5f5fac4a35
title: Benefits of MUI Explained
ms.topic: article
ms.date: 05/31/2018
---

# Benefits of MUI Explained

-   [MUI benefits for developers](#mui-benefits-for-developers)
-   [MUI benefits for enterprises](#mui-benefits-for-enterprises)
-   [MUI benefits for OEMs](#mui-benefits-for-oems)

## MUI benefits for developers

There are many possible ways to implement a MUI solution in applications, but each possibility is a variation of one of three basic methods:

1.  Compiling one binary (with built-in resources) for each language. This is the *de facto* standard for legacy applications, as this is the primary model supported by standard development tools such as Microsoft Visual Studio. This model does require multiple binaries for multiple languages and has limitations with regards to single image deployment and multi-lingual scenarios. It should be noted that applications developed with this model will continue to work on Windows Vista, and that tools are provided that help developers move from this model to the more modern model outlined in the third method.
2.  Having one language-neutral core binary with one multi-language resource dynamic-link library (DLL). This model is definitely MUI-friendly but makes it difficult to update the resource binaries to accommodate new languages. Suppose that besides English, French and Japanese, you want to also support German. A whole new resource binary would need to be provided and deployed to your users who may not necessarily need German.
3.  Having one language-neutral core binary with one set of resource DLLs per language. This is the way the operating system itself is implemented in Windows Vista, and developers are encouraged to use this model for applications as it offers more than the previous two models.

Prior to the Windows Vista release, the lack of built-in support for this latter model made it hard to adopt. However, this has changed, and the benefits of this model are numerous and make it a great model for your applications:

-   Applications can be made multi-lingual and can behave in the same way as Windows Vista, providing a consistent display language experience for users.
-   Flexibility is increased in releasing additional languages for an application. Additional languages can be released independently of the core code, which means that support for new languages can be added over time as needed.
-   Cost is reduced in creating and servicing more language releases.
-   OEMs and enterprises can easily integrate applications into their globalized PC image—ready for shipment to different countries.
-   Tools and guidelines that help you migrate your application to the Windows Vista MUI model are available. In particular, MSDN provides a [significant set of documentation](multilingual-user-interface.md) on MUI.

## MUI benefits for enterprises

MUI offers two major benefits for enterprises:

-   Single image installation: MUI allows enterprises to roll out, support and maintain the same worldwide (or any part thereof) image with a single installation. Windows Vista extends the single-image rollout of the operating system, so that business applications can also be deployed as part of the same image.
-   Support for multilingual desktops: Multiple localized UI language packs can be installed on a desktop, which enables multiple users to share a single desktop while still using their own preferred UI languages. This also applies to public computers, which need equal treatment for all the officially spoken languages (such as might be the case in Canada and in the European Union), and to shared computers for roaming users.

## MUI benefits for OEMs

The major benefit for OEMs is the single image installation that MUI enables, as it makes it possible to create images that contain all necessary languages to target a geographic zone effectively, and to delay the language choice to the user's initial installation of the computer. In particular, this enables a more effective management of inventory for OEMs.

By providing MUI support for applications, Windows Vista also enables OEMs to provide value-add applications on their images while benefiting from the single image installation, as long as these applications are MUI enabled.

 

 




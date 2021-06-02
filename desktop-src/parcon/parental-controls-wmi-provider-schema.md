---
description: The Parental Controls WMI Provider is an instance and method provider. Instantiation of new class instances, reading or modification of existing instance properties, and invocation of methods is controlled by the Wpcsprov.mof file.
ms.assetid: 28d46969-448e-4a67-bfb3-4240b5cebe57
title: Parental Controls WMI Provider Schema
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls WMI Provider Schema

The Parental Controls WMI Provider is an instance and method provider. Instantiation of new class instances, reading or modification of existing instance properties, and invocation of methods is controlled by the Wpcsprov.mof file.

The following syntax is from Namespace.mof

``` syntax
#pragma autorecover

#pragma namespace("\\\\.\\ROOT\\CIMV2")

instance of __Namespace
{
    Name = "Applications";
};

#pragma namespace("\\\\.\\ROOT\\CIMV2\\Applications")

//**************************************************************************
//* Windows Parental Controls Namespace 
//**************************************************************************
instance of __NAMESPACE
{
    Name = "WindowsParentalControls";
};
```

The following syntax is from Ratings.mof

``` syntax
//**************************************************************************
//* MOF describing Ratings Systems
//**************************************************************************
#pragma namespace("\\\\.\\ROOT\\CIMV2\\Applications\\WindowsParentalControls")

//**************************************************************************
//* Class: WpcRating
//* Derived from: 
//**************************************************************************
[Description("A rating within a ratings system"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcRating
{
    [read: ToInstance ToSubClass, Description("Rating ID"): ToInstance ToSubClass, key, Not_null: ToInstance ToSubClass] string ID;
    [read: ToInstance ToSubClass, Description("Long Name for this Rating"): ToInstance ToSubClass] string LongName;
    [Description("ID of the Ratings System this rating belongs to"): ToInstance ToSubClass, read: ToInstance ToSubClass, key, Not_null: ToInstance ToSubClass] string SystemID;
    [read: ToInstance ToSubClass, Description("Short Name for this Rating"): ToInstance ToSubClass] string ShortName;
    [read: ToInstance ToSubClass, Description("Description of this rating"): ToInstance ToSubClass] string Description;
    [read: ToInstance ToSubClass, Description("Has this rating been deprecated"): ToInstance ToSubClass, Not_null: ToInstance ToSubClass] string IsDeprecated = "false";
    [read: ToInstance ToSubClass, Description("Link to updated rating"): ToInstance ToSubClass] string UpdatedRating;
    [read: ToInstance ToSubClass, Description("Relative level index of this rating"): ToInstance ToSubClass, Not_null: ToInstance ToSubClass] uint32 Level;
    [read: ToInstance ToSubClass, Description("Recommended minimum age"): ToInstance ToSubClass] uint32 MinAge = 0;
    [read: ToInstance ToSubClass, Description("Path to the logo for the ratings system"): ToInstance ToSubClass] string IconPath;
    [read: ToInstance ToSubClass, Description("Resource ID of the logo for the ratings system"): ToInstance ToSubClass] string IconResourceID;
    [read: ToInstance ToSubClass, Description("Resource Type of the logo for the ratings system"): ToInstance ToSubClass] string IconType;
};

//**************************************************************************
//* Class: WpcRatingsDescriptor
//* Derived from: 
//**************************************************************************
[Description("Optional textual descriptor for a rating system"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcRatingsDescriptor
{
    [read: ToInstance ToSubClass, Description("ID for descriptor"): ToInstance ToSubClass, key, Not_null: ToInstance ToSubClass] string ID;
    [key, Description("GUID representing the ratings system the descriptor belongs to"): ToInstance ToSubClass, read: ToInstance ToSubClass, Not_null: ToInstance ToSubClass] string SystemID;
    [read: ToInstance ToSubClass, Description("Name of the descriptor"): ToInstance ToSubClass, Not_null: ToInstance ToSubClass] string Name;
    [read: ToInstance ToSubClass, Description("Description of the descriptor"): ToInstance ToSubClass] string Description;
    [read: ToInstance ToSubClass, Description("Has the description been deprecated"): ToInstance ToSubClass, Not_null: ToInstance ToSubClass] boolean IsDeprecated = FALSE;
    [read: ToInstance ToSubClass, Description("Link to updated descriptor"): ToInstance ToSubClass] string UpdatedDescriptor;
    [read: ToInstance ToSubClass, Description("Path to the logo for the ratings system"): ToInstance ToSubClass] string IconPath;
    [read: ToInstance ToSubClass, Description("Resource ID of the logo for the ratings system"): ToInstance ToSubClass] string IconResourceID;
    [read: ToInstance ToSubClass, Description("Resource Type of the logo for the ratings system"): ToInstance ToSubClass] string IconType;
    [read: ToInstance ToSubClass, Description("Extended properties for this descriptor"): ToInstance ToSubClass] uint32 Properties;
};

//**************************************************************************
//* Class: WpcRatingsSystem
//* Derived from: 
//**************************************************************************
[Description("Third Party Ratings System"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WPCSprov"): ToInstance ToSubClass]
class WpcRatingsSystem
{
    [key, read: ToInstance ToSubClass, Description("GUID identifying the ratings system"): ToInstance ToSubClass] string ID;
    [read: ToInstance ToSubClass, Description("Type of the ratings system"): ToInstance ToSubClass] uint32 Type;
    [read: ToInstance ToSubClass, Description("Long name for the system"): ToInstance ToSubClass] string LongName;
    [read: ToInstance ToSubClass, Description("Short name for the ratings system"): ToInstance ToSubClass] string ShortName;
    [read: ToInstance ToSubClass, Description("Description of the ratings system"): ToInstance ToSubClass, Not_null: ToInstance ToSubClass] string Description;
    [read: ToInstance ToSubClass, Description("Web address for the ratings system"): ToInstance ToSubClass] string WebAddress;
    [read: ToInstance ToSubClass, Description("Path to the logo for the ratings system"): ToInstance ToSubClass] string LogoPath;
    [read: ToInstance ToSubClass, Description("Resource ID of the logo for the ratings system"): ToInstance ToSubClass] string LogoResourceID;
    [read: ToInstance ToSubClass, Description("Resource type of the logo for the ratings system"): ToInstance ToSubClass] string LogoResourceType;
    [read: ToInstance ToSubClass, Description("Version of this data"): ToInstance ToSubClass] string Version;
};

```

The following syntax is from WpcSettings.mof

``` syntax
// WPC Class definitions

#pragma namespace("\\\\.\\ROOT\\CIMV2\\Applications\\WindowsParentalControls")

//**************************************************************************
//* Class: WpcSystemSettings
//* Derived from: 
//**************************************************************************
[Singleton: DisableOverride ToInstance ToSubClass, Description("Stores system-wide Wpc settings"): ToInstance ToSubClass, provider("WpcSProv"): ToInstance, dynamic: ToInstance]
class WpcSystemSettings
{
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Link to the current games rating system in force for the computer"): ToInstance ToSubClass] string CurrentGamesRatingSystem;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("HTTP app filter exemption list"): ToInstance ToSubClass] string HTTPExemptionList[];
    [read: ToInstance ToSubClass, Description("Windows HTTP app filter exemption list"): ToInstance ToSubClass] string WinHTTPExemptionList[];
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("HTTP URL filter exemption list"): ToInstance ToSubClass] string URLExemptionList[];
    [read: ToInstance ToSubClass, Description("Windows HTTP URL filter exemption list"): ToInstance ToSubClass] string WinURLExemptionList[];
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Number of days until a balloon reminder for checking the logs"): ToInstance ToSubClass] uint32 LogViewReminderInterval;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Last time the admin checked the log viewer"): ToInstance ToSubClass] DateTime LastLogView;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("ID of current web filter"): ToInstance ToSubClass] string FilterID;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Name of current web filter"): ToInstance ToSubClass] string FilterName;
    [Description("Creates settings for a new User SID"): ToInstance ToSubClass, Implemented: ToInstance ToSubClass, Static: ToInstance ToSubClass] uint32 AddUser([Description("SID to create settings for"): ToInstance ToSubClass, IN] string strSID);
    [Description("Removes settings for a user account"): ToInstance ToSubClass, Implemented: ToInstance ToSubClass, Static: ToInstance ToSubClass] uint32 RemoveUser([Description("SID of the account to delete settings for"): ToInstance ToSubClass, IN] string strSID);
};

//**************************************************************************
//* Class: WpcUserSettings
//* Derived from: 
//**************************************************************************
[Description("Per-account Windows Parental Controls Settings"): ToInstance ToSubClass, provider("WpcSprov"): ToInstance, dynamic: ToInstance]
class WpcUserSettings
{
    [key, read: ToInstance ToSubClass, Description("SID of the user account owning these settings"): ToInstance ToSubClass] string SID;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Is WPC enabled for this user"): ToInstance ToSubClass] boolean WpcEnabled;
    [write: ToInstance ToSubClass, Description("Is logging enabled for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] boolean LoggingRequired;
    [write: ToInstance ToSubClass, Description("Are hourly restrictions enabled for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] boolean HourlyRestrictions;
    [write: ToInstance ToSubClass, Description("Are override requests enabled for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] boolean OverrideRequests;
    [write: ToInstance ToSubClass, Description("Logon Hours mask for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] uint32 LogonHours[7];
    [write: ToInstance ToSubClass, Description("Are application restrictions enabled for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass] boolean AppRestrictions;
};

//**************************************************************************
//* Class: WpcExtension
//* Derived from: 
//**************************************************************************
[Description("Windows Parental Controls Extension"): ToInstance ToSubClass, provider("WpcSprov"): ToInstance, dynamic: ToInstance]
class WpcExtension
{
    [key, read: ToInstance ToSubClass, Description("GUID ID for the extension"): ToInstance ToSubClass] string ID;
    [key, read: ToInstance ToSubClass, Description("SiloID for the extension"): ToInstance ToSubClass, MinValue(0): ToInstance ToSubClass, MaxValue(6): ToInstance ToSubClass] uint32 Subsystem;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Image resource path for the icon for the extension"): ToInstance ToSubClass] string ImagePath;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Image resource path for the disabled icon for the extension"): ToInstance ToSubClass] string DisabledImagePath;
    [write: ToInstance ToSubClass, read: ToInstance ToSubClass, Description("Path to the extension executable"): ToInstance ToSubClass] string Path;
    [write: ToInstance ToSubClass, Description("Display name for the extension"): ToInstance ToSubClass, read: ToInstance ToSubClass] string Name;
    [write: ToInstance ToSubClass, Description("Subtitle for the extension"): ToInstance ToSubClass, read: ToInstance ToSubClass] string SubTitle;
};

//**************************************************************************
//* Class: WpcGameOverride
//* Derived from: 
//**************************************************************************
[Description("Entry in game silo override list for Windows Parental Controls"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcGameOverride
{
    [key, read: ToInstance ToSubClass, Description("Application ID identifying the game"): ToInstance ToSubClass] string AppID;
    [key, read: ToInstance ToSubClass, Description("SID of the account owning this entry"): ToInstance ToSubClass] string SID;
    [Description("Whether the entry is allowed or denied"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass, MinValue(0): ToInstance ToSubClass, MaxValue(2): ToInstance ToSubClass] uint32 Allowed;
};

//**************************************************************************
//* Class: WpcAppOverride
//* Derived from: 
//**************************************************************************
[Description("Entry in user silo application override list for Windows Parental Controls"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcAppOverride
{
    [key, read: ToInstance ToSubClass, Description("Rule ID for this entry"): ToInstance ToSubClass] string RuleID;
    [key, read: ToInstance ToSubClass, Description("SID of the account owning this entry"): ToInstance ToSubClass] string SID;
    [read: ToInstance ToSubClass, Description("Path to the overridden app"): ToInstance ToSubClass] string Path;
};

//**************************************************************************
//* Class: WpcGamesSettings
//* Derived from: 
//**************************************************************************
[Description("Games silo settings for Windows Parental Controls"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcGamesSettings
{
    [key, read: ToInstance ToSubClass, Description("SID of the account owning these settings"): ToInstance ToSubClass] string SID;
    [read: ToInstance ToSubClass, write: ToInstance ToSubClass, Description("Whether games are permitted"): ToInstance ToSubClass] boolean Blocked;
    [read: ToInstance ToSubClass, Description("GUID of the rating system these settings are for"): ToInstance ToSubClass] string SystemID;
    [read: ToInstance ToSubClass, Description("Whether to allow unrated games"): ToInstance ToSubClass, write: ToInstance ToSubClass] boolean AllowUnrated;
    [read: ToInstance ToSubClass, Description("ID of the maximum rating allowed under the current system"): ToInstance ToSubClass, write: ToInstance ToSubClass] string MaxAllowed;
    [read: ToInstance ToSubClass, Description("Collection of denied descriptors"): ToInstance ToSubClass, write: ToInstance ToSubClass] string DeniedDescriptors[];
};

//**************************************************************************
//* Class: WpcURLOverride
//* Derived from: 
//**************************************************************************
[Description("Entry in web silo URL override list for Windows Parental Controls"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcURLOverride
{
    [key, read: ToInstance ToSubClass, Description("URL to be affected"): ToInstance ToSubClass] string URL;
    [key, read: ToInstance ToSubClass, Description("SID of the account owning this entry"): ToInstance ToSubClass] string SID;
    [Description("Whether the entry is allowed or denied"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass, MinValue(0): ToInstance ToSubClass, MaxValue(2): ToInstance ToSubClass] uint32 Allowed;
};

//**************************************************************************
//* Class: WpcCustomEvent
//* Derived from: 
//**************************************************************************
[Description("The registered custom events to be used in the log viewer"): ToInstance ToSubClass, dynamic: DisableOverride ToInstance, provider("WpcSProv"): ToInstance ToSubClass]
class WpcCustomEvent
{
    [key, read: ToInstance ToSubClass, Description("Publisher of the event"): ToInstance ToSubClass] string Publisher;
    [key, read: ToInstance ToSubClass, Description("Application making the event"): ToInstance ToSubClass] string Application;
    [key, read: ToInstance ToSubClass, Description("Event name to use"): ToInstance ToSubClass] string Event;
    [read: ToInstance ToSubClass, Description("Collection of headers"): ToInstance ToSubClass, write: ToInstance ToSubClass] string Headers[];
};


//**************************************************************************
//* Class: WpcWebSettings
//* Derived from: 
//**************************************************************************
[Description("Per-account Windows Parental Controls Web Settings"): ToInstance ToSubClass, provider("WpcSprov"): ToInstance, dynamic: ToInstance]
class WpcWebSettings
{
    [key, Description("SID of the user account owning these settings"): ToInstance ToSubClass, read: ToInstance ToSubClass] string SID;
    [Description("Is filter on for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass] boolean FilterOn;
    [Description("Filter level for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass, MinValue(0): ToInstance ToSubClass, MaxValue(5): ToInstance ToSubClass] Uint32 FilterLevel;
    [Description("Are file downloads blocked for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass] boolean FileDownloadsBlocked;
    [Description("Are unrated sites blocked for this user"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass] boolean BlockUnrated;
    [Description("Blocked Category list"): ToInstance ToSubClass, read: ToInstance ToSubClass, write: ToInstance ToSubClass] uint32 BlockedCategoryList[];
};

[Description("Games Clamper for Windows Parental Controls Media Settings"): ToInstance ToSubClass, 
 provider("WpcClamperProv"): ToInstance, 
 dynamic: ToInstance]
class WpcClamper      
{                                                                  
    [
    Description("Creates settings for a new User SID"): ToInstance ToSubClass, 
    Implemented: ToInstance ToSubClass, 
    Static: ToInstance ToSubClass
    ] 
    uint32 LockDownGameInstance([Description("Instance ID to lock down"): ToInstance ToSubClass, IN] string guidInstanceID);
    [
    Description("Removes settings for any admin users"): ToInstance ToSubClass, 
    Implemented: ToInstance ToSubClass, 
    Static: ToInstance ToSubClass
    ] 
    uint32 CleanupUsers();
};                                                                 

// End of WPC Class Definitions
```

The following syntax is from WpcProvider.mof

``` syntax
#pragma namespace ("\\\\.\\root\\CIMV2\\Applications\\WindowsParentalControls")

class Win32_ProviderEx : __Win32Provider
{
    [Description ( "Hosting Model, provides compatibility with Windows XP and Windows Server 2003. Do not override." ) , Override("HostingModel")]
    string HostingModel = "NetworkServiceHost";
    [Description("..."),Override("SecurityDescriptor")] 
    string SecurityDescriptor; 
    UInt32 version = 1;
} ;

instance of Win32_ProviderEx as $WpcSProv
{
    Name    = "WpcSProv" ;  //Name is the key property for __Provider objects.
                            //vendor|provider|version is the suggested format
                            //to prevent name collisions.

    ClsId   = "{355DFFAA-3B9F-435c-B428-5D44290BC5F2}" ;     //provider GUID

    DefaultMachineName = NULL;       //NULL for local computer

    ClientLoadableCLSID = NULL;      //reserved

    ImpersonationLevel = 0;          //reserved

    InitializationReentrancy = 0;       //Set of flags that provide information about serialization:
                                        //0 = all initialization of this provider must be serialized
                                        //1 = all initializations of this provider in the same namespace must be serialized
                                        //2 = no initialization serialization is necessary

    InitializeAsAdminFirst = FALSE;     //Request to be fully initialized as "Admin" before 
                                        //initializations begin for users

    PerLocaleInitialization = FALSE;    //Indicates whether the provider is initialized for each 
                                        //locale if a user connects to the same namespace more 
                                        //than once using different locales.

    PerUserInitialization = FALSE;      //Indicates whether the provider is initialized once for each actual 
                                        //Windows 2000 NTLM user making requests of the provider. 
                                        //If set to FALSE, the provider is initialized once for all users

    Pure = TRUE;                        //A pure provider exists only to service requests from 
                                        //applications and WMI. Most providers are pure providers
                                        //Non-pure providers transition to the role of client after they have 
                                        //finished servicing requests. 


    UnloadTimeout = NULL;               //Currently ignored
                                        //Use __CacheControl class in the root namespace to control provider unloading
                                        //A string in the DMTF date/time format that specifies how long WMI 
                                        //allows the provider to remain idle before it is unloaded.
                                        

} ;    

instance of __InstanceProviderRegistration
{
    Provider = $WpcSProv;

    SupportsPut = "TRUE"; 
    SupportsGet = "TRUE"; 
    SupportsDelete = "TRUE"; 
    SupportsEnumeration = "TRUE"; 

};

instance of __MethodProviderRegistration
{
    Provider = $WpcSProv;
};

instance of __Win32Provider as $WpcClamperProv
{
    Name    = "WpcClamperProv" ;
    ClsId   = "{355DFFAA-3B9F-435c-B428-5D44290BC5F2}" ;
    HostingModel = "LocalSystemHost" ;
};    

instance of __MethodProviderRegistration
{
    Provider = $WpcClamperProv;
};
```

 

 




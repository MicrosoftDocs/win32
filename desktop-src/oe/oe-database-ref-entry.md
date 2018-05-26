---
title: Windows Mail Database Reference
description: This documentation provides database-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).
ms.assetid: f785fba4-20bb-4def-bc09-219b242a9946
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Mail Database Reference

This documentation provides database-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).

New applications should not use this set of interfaces and schemas. These interfaces and schemas exist for backward compatibility with legacy applications. These interfaces and schemas will be unavailable in the future.

An idl such as the DirectDB.idl example in this section defines the IDatabase interface as well as several other supporting interfaces. Headers such as the OEStore6.h and SyncOp.h examples described in this overview define several TABLESCHEMA implementations and supporting structures.

The IDatabase interface enables access to database files written by Outlook Express 6. The extension for IDatabase files is .dbx. The following schemas are used to describe the folder databases:

-   g\_OE6FolderTableSchema - The schema for the folder databases.
-   g\_OE6MessageTableSchema - The schema or the message databases.
-   g\_OE6UidlTableSchema - The schema for a database which stores the state of spooler operations in Outlook Express 6.
-   g\_OE6SyncOpTableSchema - The schema for the sync operations database.

### Interfaces



| Topic                                             | Contents                                                                              |
|---------------------------------------------------|---------------------------------------------------------------------------------------|
| [**IDatabase**](oe-idatabase.md)                 | Do not use. Enables legacy Windows Mail database access.<br/>                   |
| [**IDatabaseProgress**](oe-idatabaseprogress.md) | Do not use. Enables legacy Windows Mail database progress operations.<br/>      |
| [**IDatabaseSession**](oe-idatabasesession.md)   | Do not use. Enables legacy Windows Mail database session operations.<br/>       |
| [**IDatabaseStream**](oe-idatabasestream.md)     | Do not use. Enables streaming operations for legacy Windows Mail database.<br/> |



 

### Enums



| Topic                                                 | Contents                                                                                                                                 |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACCESSTYPE**](oe-accesstype.md)                   | Do not use. Flags for specifying the type of access needed when accessing a stream.<br/>                                           |
| [**COLUMNDATATYPE**](oe-columndatatype.md)           | Do not use. Used to specify the type of a column of a database.<br/>                                                               |
| [**COMPAREFLAGS**](oe-compareflags.md)               | Do not use. This flag is used when defining indices of a database table. It specifies how database should compare two values.<br/> |
| [**REGISTERNOTIFYFLAGS**](oe-registernotifyflags.md) | Do not use. Flags for registering notification.<br/>                                                                               |
| [**SEEKROWSETTYPE**](oe-seekrowsettype.md)           | Do not use. Used as a parameter to IDatabase::SeekRowset to specify the starting location of the seek.<br/>                        |
| [**SYMBOLTYPE**](oe-symboltype.md)                   | Do not use. Specifies the type of symbols being used.<br/>                                                                         |
| [**TABLESCHEMAFLAGS**](oe-tableschemaflags.md)       | Do not use.<br/>                                                                                                                   |
| [**TRANSACTIONTYPE**](oe-transactiontype.md)         | Do not use. Specifies how a transaction affected the database.<br/>                                                                |



 

### Structures



| Topic                                 | Contents                                                                                                                                                  |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INDEXKEY**](oe-indexkey.md)       | Do not use. Describes a key used in an index.<br/>                                                                                                  |
| [**ORDINALLIST**](oe-ordinallist.md) | Do not use. This struct stores the array of index ordinals for two records. These ordinals can be used for seeking to the record in the table.<br/> |
| [**SYMBOLINFO**](oe-symbolinfo.md)   | Do not use. Specifies a name for a symbol.<br/>                                                                                                     |
| [**SYMBOLTABLE**](oe-symboltable.md) | Do not use. Specifies a set of symbols.<br/>                                                                                                        |
| [**TABLECOLUMN**](oe-tablecolumn.md) | Do not use. This structure describes a database table column.<br/>                                                                                  |
| [**TABLEINDEX**](oe-tableindex.md)   | Do not use. This struct represents an index on a table. It can be used to sort the records in the table by any of the columns.<br/>                 |
| [**TABLESCHEMA**](oe-tableschema.md) | Do not use. Describes the schema of a database table.<br/>                                                                                          |



 

### Constants



| Topic                                             | Contents                                                                                                        |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CMAX**](oe-cmax.md)                           | Do not use. The (CMAX\_\*) constants are used to specify index limits on databases.<br/>                  |
| [**INDEXORDINAL**](oe-indexordinal.md)           | Do not use. Connection type values that can be set, and their meaning. <br/>                              |
| [**MISC\_DB**](oe-misc-db.md)                    | Do not use.<br/>                                                                                          |
| [**OPENDATABASEFLAGS**](oe-opendatabaseflags.md) | Do not use. DWORD that specifies various flags that are used when opening a database.<br/>                |
| [**RESERVED**](oe-reserved.md)                   | Do not use. The RESERVED\_ constants are used to define boundries for reserved database identifiers.<br/> |



 

The following is an example idl for Windows Mail database references.


```

import "ocidl.idl";
import "objidl.idl";

cpp_quote("#include <stddef.h> // for offsetof")

interface IDatabaseSession;
interface IDatabase;
interface IDatabaseProgress;
interface IDatabaseNotify;
interface IDatabaseStream;

cpp_quote("// {4A16043F-676D-11d2-994E-00C04FA309D4}")
cpp_quote("DEFINE_GUID(CLSID_DatabaseSession, 0x4a16043f, 0x676d, 0x11d2, 0x99, 0x4e, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")
cpp_quote("")
cpp_quote("// {4A160440-676D-11d2-994E-00C04FA309D4}")
cpp_quote("DEFINE_GUID(IID_IDatabaseSession, 0x4a160440, 0x676d, 0x11d2, 0x99, 0x4e, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")
cpp_quote("")
cpp_quote("// {7157F0AE-967B-11d1-9A08-00C04FA309D4}")
cpp_quote("DEFINE_GUID(IID_IDatabase, 0x7157f0ae, 0x967b, 0x11d1, 0x9a, 0x8, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")
cpp_quote("")
cpp_quote("// {82EAD219-A6EC-11d1-9A11-00C04FA309D4}")
cpp_quote("DEFINE_GUID(IID_IDatabaseStream, 0x82ead219, 0xa6ec, 0x11d1, 0x9a, 0x11, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")
cpp_quote("")
cpp_quote("// {5E8A5021-AC7C-11d1-9A16-00C04FA309D4}")
cpp_quote("DEFINE_GUID(IID_IDatabaseProgress, 0x5e8a5021, 0xac7c, 0x11d1, 0x9a, 0x16, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")
cpp_quote("")
cpp_quote("// {5E8A5022-AC7C-11d1-9A16-00C04FA309D4}")
cpp_quote("DEFINE_GUID(IID_IDatabaseNotify, 0x5e8a5022, 0xac7c, 0x11d1, 0x9a, 0x16, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);")

cpp_quote("#define DB_E_ALREADYOPEN            HR_E(300)")
cpp_quote("#define DB_E_CREATEMUTEX            HR_E(301)")
cpp_quote("#define DB_E_CREATEFILE             HR_E(302)")
cpp_quote("#define DB_E_GETFILESIZE            HR_E(303)")
cpp_quote("#define DB_E_CREATEFILEMAPPING      HR_E(304)")
cpp_quote("#define DB_E_MAPVIEWOFFILE          HR_E(305)")
cpp_quote("#define DB_E_SETENDOFFILE           HR_E(306)")
cpp_quote("#define DB_E_SETFILEPOINTER         HR_E(307)")
cpp_quote("#define DB_E_BADMAJORVERSION        HR_E(308)")
cpp_quote("#define DB_E_INVALIDFILESIGNATURE   HR_E(309)")
cpp_quote("#define DB_E_WRITEFILE              HR_E(310)")
cpp_quote("#define DB_E_TIMEOUT                HR_E(311)")
cpp_quote("#define DB_E_FLUSHVIEWOFFILE        HR_E(312)")
cpp_quote("#define DB_E_FLUSHFILEBUFFERS       HR_E(313)")
cpp_quote("#define DB_E_DUPLICATE              HR_E(314)")
cpp_quote("#define DB_E_CORRUPT                HR_E(315)")
cpp_quote("#define DB_E_DISKFULL               HR_E(316)")
cpp_quote("#define DB_E_GETTEMPFILENAME        HR_E(317)")
cpp_quote("#define DB_E_NOTFOUND               HR_E(318)")
cpp_quote("#define DB_E_STREAMTABLEFULL        HR_E(319)")
cpp_quote("#define DB_E_NORECORDS              HR_E(320)")
cpp_quote("#define DB_E_COMPACT_PREEMPTED      HR_E(321)")
cpp_quote("#define DB_E_DATABASE_CHANGED       HR_E(322)")
cpp_quote("#define DB_E_COMPACTING             HR_E(323)")
cpp_quote("#define DB_E_RECORDVERSIONCHANGED   HR_E(324)")
cpp_quote("#define DB_E_CORRUPTRECORD          HR_E(325)")
cpp_quote("#define DB_E_BADMINORVERSION        HR_E(326)")
cpp_quote("#define DB_E_TOOMANYOPENROWSETS     HR_E(328)")
cpp_quote("#define DB_E_LOCKEDFORREAD          HR_E(329)")
cpp_quote("#define DB_E_LOCKEDFORWRITE         HR_E(330)")
cpp_quote("#define DB_E_FILENOTFOUND           HR_E(331)")
cpp_quote("#define DB_E_UNMATCHINGQUOTES       HR_E(332)")
cpp_quote("#define DB_E_UNMATCHINGPARENS       HR_E(333)")
cpp_quote("#define DB_E_NUMBERTOOBIG           HR_E(334)")
cpp_quote("#define DB_E_BADNUMBER              HR_E(335)")
cpp_quote("#define DB_E_NOSYMBOLS              HR_E(336)")
cpp_quote("#define DB_E_INVALIDSYMBOL          HR_E(337)")
cpp_quote("#define DB_E_INVALIDCOLUMN          HR_E(338)")
cpp_quote("#define DB_E_BADEXPRESSION          HR_E(339)")
cpp_quote("#define DB_E_MOVEFILE               HR_E(340)")
cpp_quote("#define DB_E_ACCESSDENIED           HR_E(341)")
cpp_quote("#define DB_E_WRONGTHREAD            HR_E(342)")
cpp_quote("#define DB_E_ALREADYREGISTERED      HR_E(343)")

cpp_quote("#define DB_S_FOUND                  HR_S(800)")
cpp_quote("#define DB_S_NOTFOUND               HR_S(801)")

cpp_quote("#define sizeofMember(s,m)    sizeof(((s *)0)->m)")

#ifndef DECLARE_HANDLE
#define DECLARE_HANDLE(name) \
    struct name##__ { DWORD unused; }; \
    typedef struct name##__ _far* name
#endif
midl_pragma warning(disable:2395)

[
    uuid(E462D143-5162-11d1-8A95-00C04FB951F3),
    helpstring("Microsoft DirectDB Type Library 1.0"),
    version(1.0)
]
library DirectDB
{
    importlib("stdole2.tlb");

    cpp_quote("#ifndef __LPDATABASE_DEFINED")
    cpp_quote("#define __LPDATABASE_DEFINED")
    [
        object,
        uuid(7157F0AE-967B-11d1-9A08-00C04FA309D4),
        pointer_default(unique)
    ]
    interface IDatabase : IUnknown
    {
        typedef IDatabase *LPDATABASE;

        const DWORD CMAX_INDEXES                            = 8;
        const DWORD CMAX_KEYS                               = 8;
        const DWORD COLUMNS_ALL                             = 0xFFFFFFFF;

        const DWORD RESERVED_ID_MIN                         = 0xFFFFFBFF;
        const DWORD RESERVED_ID_MAX                         = 0xFFFFFFFF;

        DECLARE_HANDLE(HROWSET);
        typedef HROWSET *LPHROWSET;
        const HROWSET HROWSET_INVALID = (HROWSET) 0x00000000;

        DECLARE_HANDLE(HLOCK);
        typedef HLOCK *LPHLOCK;

        typedef enum tagSEEKROWSETTYPE {
            SEEK_ROWSET_BEGIN,
            SEEK_ROWSET_CURRENT,
            SEEK_ROWSET_END
        } SEEKROWSETTYPE;

        typedef enum tagTRANSACTIONTYPE {
            TRANSACTION_INSERT,
            TRANSACTION_UPDATE,
            TRANSACTION_DELETE,
            TRANSACTION_INDEX_CHANGED,
            TRANSACTION_INDEX_DELETED,
            TRANSACTION_COMPACTED
        } TRANSACTIONTYPE, *LPTRANSACTIONTYPE;

        DECLARE_HANDLE(HTRANSACTION);
        typedef HTRANSACTION *LPHTRANSACTION;

        typedef DWORD FILEADDRESS;
        typedef LPDWORD LPFILEADDRESS;

        typedef DWORD INDEXORDINAL;
        typedef LPDWORD LPINDEXORDINAL;
        cpp_quote("#define INVALID_INDEX_ORDINAL            0xFFFFFFFF")
        cpp_quote("#define IINDEX_PRIMARY                   0")

        typedef BYTE COLUMNORDINAL;
        typedef BYTE *LPCOLUMNORDINAL;

        typedef DWORD COMPACTFLAGS;
        cpp_quote("#define COMPACT_PREEMPTABLE              0x00000001")
        cpp_quote("#define COMPACT_YIELD                    0x00000002")

        typedef DWORD LOCKNOTIFYFLAGS;

        typedef DWORD REGISTERNOTIFYFLAGS;
        cpp_quote("#define REGISTER_NOTIFY_NOADDREF         0x00000001")
        cpp_quote("#define REGISTER_NOTIFY_ORDINALSONLY     0x00000002")

        typedef BYTE COMPAREFLAGS;
        cpp_quote("#define COMPARE_IGNORECASE               0x00000001")
        cpp_quote("#define COMPARE_DESCENDING               0x00000002")
        cpp_quote("#define COMPARE_ASANSI                   0x00000004")

        typedef DWORD TABLESCHEMAFLAGS;
        cpp_quote("#define TSF_RESETIFBADVERSION            0x00000001")
        cpp_quote("#define TSF_HASSTREAMS                   0x00000002")

        typedef BYTE INDEXFLAGS;
        cpp_quote("#define INDEX_DESCENDING                 0x00000001")

        typedef DWORD ROWORDINAL;
        typedef LPDWORD LPROWORDINAL;
        const ROWORDINAL INVALID_ROWORDINAL               = 0xffffffff;

        typedef enum tagACCESSTYPE {
            ACCESS_READ=100,
            ACCESS_WRITE=200
        } ACCESSTYPE;

        typedef enum tagCOLUMNDATATYPE {
            CDT_FILETIME,
            CDT_FIXSTRA,
            CDT_VARSTRA,
            CDT_BYTE,
            CDT_DWORD,
            CDT_WORD,
            CDT_STREAM,
            CDT_VARBLOB,
            CDT_FIXBLOB,
            CDT_FLAGS,
            CDT_UNIQUE,
            CDT_FIXSTRW,
            CDT_VARSTRW,
            CDT_LASTTYPE
        } COLUMNDATATYPE;

        typedef enum tagSYMBOLTYPE {
            SYMBOL_INVALID,
            SYMBOL_COLUMN,
            SYMBOL_DWORD,
            SYMBOL_METHOD
        } SYMBOLTYPE;

        typedef struct tagSYMBOLINFO {
            SYMBOLTYPE          tySymbol;
            LPCSTR              pszName;
            DWORD               dwValue;
        } SYMBOLINFO, *LPSYMBOLINFO;

        typedef struct tagSYMBOLTABLE {
            DWORD               cSymbols;
            SYMBOLINFO          rgSymbol[32];
        } SYMBOLTABLE, *LPSYMBOLTABLE;
        typedef SYMBOLTABLE const *LPCSYMBOLTABLE;

        typedef struct tagORDINALLIST {
            ROWORDINAL      rgiRecord1[CMAX_INDEXES];
            ROWORDINAL      rgiRecord2[CMAX_INDEXES];
        } ORDINALLIST, *LPORDINALLIST;

        #pragma pack(1)
        typedef struct tagINDEXKEY {
            COLUMNORDINAL       iColumn;     // 1
            COMPAREFLAGS        bCompare;    // 2
            DWORD               dwBits;      // 6
        } INDEXKEY, *LPINDEXKEY;
        #pragma pack()
        typedef INDEXKEY const *LPCINDEXKEY;

        #pragma pack(1)
        typedef struct tagTABLEINDEX {
            BYTE                cKeys;              // 2
            INDEXFLAGS          bFlags;             // 4
            INDEXKEY            rgKey[CMAX_KEYS];
        } TABLEINDEX, *LPTABLEINDEX;
        #pragma pack()
        typedef TABLEINDEX const *LPCTABLEINDEX;

        typedef struct tagTABLECOLUMN {
            COLUMNORDINAL       iOrdinal;
            COLUMNDATATYPE      type;
            DWORD               ofBinding;
            DWORD               cbSize;
        } TABLECOLUMN, *LPTABLECOLUMN;
        typedef TABLECOLUMN const *LPCTABLECOLUMN;

        typedef struct tagTABLESCHEMA {
            LPVOID      pReserved;
            DWORD               cbBinding;
            DWORD               ofMemory;
            DWORD               ofVersion;
            DWORD               dwReserved;
            TABLESCHEMAFLAGS    dwFlags;
            DWORD               cbUserData;
            DWORD               ofUniqueId;
            BYTE                cColumns;
            LPCTABLECOLUMN      prgColumn;
            LPCTABLEINDEX       pPrimaryIndex;
            LPCSYMBOLTABLE      pSymbols;
        } TABLESCHEMA, *LPTABLESCHEMA;
        typedef TABLESCHEMA const *LPCTABLESCHEMA;

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define BEGIN_TABLE_INDEX(_index, _cKeys) \\")
        cpp_quote("    extern const TABLEINDEX _index = { _cKeys, 0, {")
        cpp_quote("#else")
        cpp_quote("#define BEGIN_TABLE_INDEX(_index, _cKeys)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define DEFINE_KEY(_iColumn, _wCompare, _dwBits) { _iColumn, _wCompare, _dwBits },")
        cpp_quote("#else")
        cpp_quote("#define DEFINE_KEY(_iColumn, _wCompare, _dwBits)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define END_TABLE_INDEX } };")
        cpp_quote("#else")
        cpp_quote("#define END_TABLE_INDEX")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define BEGIN_COLUMN_ARRAY(_name, _cColumns) const TABLECOLUMN _name[_cColumns] = {")
        cpp_quote("#else")
        cpp_quote("#define BEGIN_COLUMN_ARRAY(_name, _cColumns)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define DEFINE_COLUMN(_iColumn, _type, _structure, _member)\\")
        cpp_quote("    { _iColumn, _type, offsetof(_structure, _member), sizeofMember(_structure, _member) },")
        cpp_quote("#else")
        cpp_quote("#define DEFINE_COLUMN(_iColumn, _type, _structure, _member)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define END_COLUMN_ARRAY };")
        cpp_quote("#else")
        cpp_quote("#define END_COLUMN_ARRAY")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define BEGIN_SYMBOL_TABLE(_name, _cSymbols) \\")
        cpp_quote("    extern const SYMBOLTABLE _name = { _cSymbols, {")
        cpp_quote("#else")
        cpp_quote("#define BEGIN_SYMBOL_TABLE(_name, _cSymbols)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define DEFINE_SYMBOL(_tySymbol, _pszName, _dwValue) \\")
        cpp_quote("    { _tySymbol, (LPCSTR)_pszName, _dwValue },")
        cpp_quote("#else")
        cpp_quote("#define DEFINE_SYMBOL(_tySymbol, _pszName, _dwValue)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define END_SYMBOL_TABLE } };")
        cpp_quote("#else")
        cpp_quote("#define END_SYMBOL_TABLE")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define BEGIN_TABLE_SCHEMA(_schema, _clsid, _binding) \\")
        cpp_quote("    extern const TABLESCHEMA _schema = { \\")
        cpp_quote("        &amp;_clsid,\\")
        cpp_quote("        sizeof(_binding),\\")
        cpp_quote("        offsetof(_binding, pAllocated),\\")
        cpp_quote("        offsetof(_binding, bVersion),")
        cpp_quote("#else")
        cpp_quote("#define BEGIN_TABLE_SCHEMA(_schema, _clsid, _binding)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define SCHEMA_PROPERTY(_value) \\")
        cpp_quote("    _value,")
        cpp_quote("#else")
        cpp_quote("#define SCHEMA_PROPERTY(_value)")
        cpp_quote("#endif")

        cpp_quote("#ifdef DEFINE_DIRECTDB")
        cpp_quote("#define END_TABLE_SCHEMA };")
        cpp_quote("#else")
        cpp_quote("#define END_TABLE_SCHEMA")
        cpp_quote("#endif")


        HRESULT Lock(
                [out]           LPHLOCK                 phLock);

        HRESULT Unlock(
                [out]           LPHLOCK                 phLock);


        HRESULT InsertRecord(
                [in]            LPVOID                  pRecord);

        HRESULT UpdateRecord(
                [in]            LPVOID                  pRecord);

        HRESULT DeleteRecord(
                [in]            LPVOID                  pRecord);

        HRESULT FindRecord(
                [in]            INDEXORDINAL            iIndex,
                [in]            DWORD                   cColumns,   // Use COLUMNS_ALL to compare all columns of the index
                [in,out]        LPVOID                  pRecord,
                [out]           LPROWORDINAL            piRow);

        HRESULT GetRowOrdinal(
                [in]            INDEXORDINAL            iIndex,
                [in]            LPVOID                  pRecord,
                [out]           LPROWORDINAL            piRow);

        HRESULT FreeRecord(
                [in,out]        LPVOID                  pRecord);

        HRESULT GetUserData(
                [in,out]        LPVOID                  pvUserData,
                [in]            ULONG                   cbUserData);

        HRESULT SetUserData(
                [in]            LPVOID                  pvUserData,
                [in]            ULONG                   cbUserData);

        HRESULT GetRecordCount(
                [in]            INDEXORDINAL            iIndex,
                [out]           LPDWORD                 pcRecords);


        HRESULT GetIndexInfo(
                [in]            INDEXORDINAL            iIndex,
                [out]           LPSTR                  *ppszFilter,
                [out]           LPTABLEINDEX            pIndex);

        HRESULT ModifyIndex(
                [in]            INDEXORDINAL            iIndex,
                [in]            LPCSTR                  pszFilter,
                [in]            LPCTABLEINDEX           pIndex);

        HRESULT DeleteIndex(
                [in]            INDEXORDINAL            iIndex);


        HRESULT CreateRowset(
                [in]            INDEXORDINAL            iIndex,
                [in]            DWORD                   dwReserved,
                [out]           LPHROWSET               phRowset);

        HRESULT SeekRowset(
                [in]            HROWSET                 hRowset,
                [in]            SEEKROWSETTYPE          tySeek,
                [in]            LONG                    cRows,
                [out]           LPROWORDINAL            piRowNew);

        HRESULT QueryRowset(
                [in]            HROWSET                 hRowset,
                [in]            LONG                    cWanted,
                [in,out]        LPVOID                 *prgpRecord,
                [out]           LPDWORD                 pcObtained);

        HRESULT CloseRowset(
                [in,out]        LPHROWSET               phRowset);


        HRESULT CreateStream(
                [out]           LPFILEADDRESS           pfaStart);

        HRESULT DeleteStream(
                [in]            FILEADDRESS             faStart);

        HRESULT CopyStream(
                [in]            IDatabase              *pDest,
                [in]            FILEADDRESS             faStream,
                [out]           LPFILEADDRESS           pfaNew);

        HRESULT OpenStream(
                [in]            ACCESSTYPE              tyAccess,
                [in]            FILEADDRESS             faStream,
                [out]           IStream               **ppStream);

        HRESULT ChangeStreamLock(
                [in]            IStream                *pStream,
                [in]            ACCESSTYPE              tyAccessNew);


        HRESULT RegisterNotify(
                [in]            INDEXORDINAL            iIndex,
                [in]            REGISTERNOTIFYFLAGS     dwFlags,
                [in]            DWORD_PTR               dwCookie,
                [in]            IDatabaseNotify        *pNotify);

        HRESULT DispatchNotify(
                [in]            IDatabaseNotify        *pNotify);

        HRESULT SuspendNotify(
                [in]            IDatabaseNotify        *pNotify);

        HRESULT ResumeNotify(
                [in]            IDatabaseNotify        *pNotify);

        HRESULT UnregisterNotify(
                [in]            IDatabaseNotify        *pNotify);

        HRESULT LockNotify(
                [in]            LOCKNOTIFYFLAGS         dwFlags,
                [out]           LPHLOCK                 phLock);

        HRESULT UnlockNotify(
                [in,out]        LPHLOCK                 phLock);

        HRESULT GetTransaction(
                [in,out]        LPHTRANSACTION          phTransaction,
                [out]           LPTRANSACTIONTYPE       ptyTransaction,
                [in]            LPVOID                  pRecord1,
                [in]            LPVOID                  pRecord2,
                [in,out]        LPINDEXORDINAL          piIndex,
                [in]            LPORDINALLIST           pOrdinals);


        HRESULT MoveFile(
                [in]            LPCWSTR                 pwszFilePath);

        HRESULT SetSize(
                [in]            DWORD                   cbSize);

        HRESULT Repair(void);

        HRESULT Compact(
                [in]            IDatabaseProgress      *pProgress,
                [in]            COMPACTFLAGS            dwFlags);


        HRESULT HeapAllocate(
                [in]            DWORD                   dwFlags, // HEAP_xxx Flags normally passed to HeapAlloc
                [in]            DWORD                   cbSize,
                [out]           LPVOID                 *ppBuffer);

        HRESULT HeapFree(
                [in]            LPVOID                  pBuffer);


        HRESULT GenerateId(
                [out]           LPDWORD                 pdwId);

        HRESULT GetClientCount(
                [out]           LPDWORD                 pcClients);

        HRESULT GetFile(
                [out]           LPWSTR                 *ppwszFile);

        HRESULT GetSize(
                [out]           LPDWORD                 pcbFile,
                [out]           LPDWORD                 pcbAllocated,
                [out]           LPDWORD                 pcbFreed,
                [out]           LPDWORD                 pcbStreams);
    }
    cpp_quote("#endif //  __LPDATABASE_DEFINED")

    cpp_quote("#ifndef __LPDATABASESESSION_DEFINED")
    cpp_quote("#define __LPDATABASESESSION_DEFINED")
    [
        object,
        uuid(4A160440-676D-11d2-994E-00C04FA309D4),
        pointer_default(unique)
    ]
    interface IDatabaseSession : IUnknown
    {
        typedef IDatabaseSession *LPDATABASESESSION;

        typedef DWORD OPENDATABASEFLAGS;
        cpp_quote("#define OPEN_DATABASE_NORESET            0x00000001")
        cpp_quote("#define OPEN_DATABASE_EXCLUSIVE         0x00000020")
        cpp_quote("#define OPEN_DATABASE_NOCREATE           0x00000040")

        HRESULT OpenDatabase(
                [in]            LPCSTR                  pszFile,
                [in]            OPENDATABASEFLAGS       dwFlags,
                [in]            LPCTABLESCHEMA          pSchema,
                [in]            LPVOID                  pReserved,
                [out]           IDatabase             **ppDB);

        HRESULT OpenDatabaseW(
                [in]            LPCWSTR                 pwszFile,
                [in]            OPENDATABASEFLAGS       dwFlags,
                [in]            LPCTABLESCHEMA          pSchema,
                [in]            LPVOID                  pReserved,
                [out]           IDatabase             **ppDB);

        HRESULT OpenQuery(
                [in]            IDatabase              *pDatabase,
                [in]            LPCSTR                  pszQuery,
                [in]            LPVOID                 *pReserved);
    }
    cpp_quote("#endif // __LPDATABASESESSION_DEFINED")

 
    cpp_quote("#ifndef __LPDATABASENOTIFY_DEFINED")
    cpp_quote("#define __LPDATABASENOTIFY_DEFINED")
    [
        object,
        uuid(7CADFB4C-AC65-11d1-9A16-00C04FA309D4),
        pointer_default(unique)
    ]
    interface IDatabaseNotify : IUnknown
    {
        typedef IDatabaseNotify *LPDATABASENOTIFY;

        HRESULT OnTransaction(
                [in]            HTRANSACTION            hTransaction,
                [in]            DWORD_PTR               dwCookie,
                [in]            IDatabase              *pDB);
    }
    cpp_quote("#endif // __LPDATABASENOTIFY_DEFINED")

    cpp_quote("#ifndef __LPDATABASESTREAM_DEFINED")
    cpp_quote("#define __LPDATABASESTREAM_DEFINED")
    [
        object,
        uuid(82EAD219-A6EC-11d1-9A11-00C04FA309D4),
        pointer_default(unique)
    ]
    interface IDatabaseStream : IStream
    {
        typedef IDatabaseStream *LPDATABASESTREAM;

        HRESULT GetFileAddress(
                [out]           LPFILEADDRESS           pfaStream);

        HRESULT CompareDatabase(
                [in]            IDatabase              *pDatabase);
    }
    cpp_quote("#endif // __LPDATABASESTREAM_DEFINED")

    cpp_quote("#ifndef __LPDATABASEPROGRESS_DEFINED")
    cpp_quote("#define __LPDATABASEPROGRESS_DEFINED")
    [
        object,
        uuid(7CADFB4B-AC65-11d1-9A16-00C04FA309D4),
        pointer_default(unique)
    ]
    interface IDatabaseProgress : IUnknown
    {
        HRESULT Update(
                [in]            DWORD                   cCount);
    }
    cpp_quote("#endif // __LPDATABASEPROGRESS_DEFINED")


} // DirectDB Library Object Definition
```



The following example header describes the Windows Mail database store references.


```


#pragma once

typedef DWORD FLDRFLAGS;
typedef BYTE FOLDERTYPE;
typedef DWORD RULEID;
typedef DWORD MESSAGEFLAGS;
typedef DWORDLONG FOLDERID;

#include "syncop.h"

const DWORD FOLDER_DATABASE_VERSION_OE6     = 5;

DEFINE_GUID(CLSID_MessageDatabase_OE6, 0x6f74fdc5, 0xe366, 0x11d1, 0x9a, 0x4e, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);
DEFINE_GUID(CLSID_FolderDatabase_OE6, 0x6f74fdc6, 0xe366, 0x11d1, 0x9a, 0x4e, 0x0, 0xc0, 0x4f, 0xa3, 0x9, 0xd4);
DEFINE_GUID(CLSID_SyncOpDatabase_OE6, 0x26fe9d30, 0x1a8f, 0x11d2, 0xaa, 0xbf, 0x0, 0x60, 0x97, 0xd4, 0x74, 0xc4);

typedef struct tagSTOREUSERDATA_OE6 {
    FILETIME            ftCreated;
    BYTE                fConvertedToDBX;
    BYTE                rgbReserved[255];
} STOREUSERDATA_OE6, *LPSTOREUSERDATA_OE6;

typedef enum tagFLDCOLID_OE6 {
    FLDCOL_OE6_ID=0,
    FLDCOL_OE6_PARENT,
    FLDCOL_OE6_NAME,
    FLDCOL_OE6_FILE,
    FLDCOL_OE6_DESCRIPTION,
    FLDCOL_OE6_ACCOUNTID,
    FLDCOL_OE6_FLAGS,
    FLDCOL_OE6_MESSAGES,
    FLDCOL_OE6_UNREAD,
    FLDCOL_OE6_SPECIAL,
    FLDCOL_OE6_TYPE,
    FLDCOL_OE6_HIERARCHY,
    FLDCOL_OE6_LISTSTAMP,
    FLDCOL_OE6_SERVERHIGH,
    FLDCOL_OE6_SERVERLOW,
    FLDCOL_OE6_SERVERCOUNT,
    FLDCOL_OE6_CLIENTHIGH,
    FLDCOL_OE6_CLIENTLOW,
    FLDCOL_OE6_NOTDOWNLOADED,
    FLDCOL_OE6_REQUESTED,
    FLDCOL_OE6_URLCOMPONENT,
    FLDCOL_OE6_READ,
    FLDCOL_OE6_THREADUNREAD,
    FLDCOL_OE6_VIEWUNREAD,
    FLDCOL_OE6_STATUSMSGDELTA,
    FLDCOL_OE6_STATUSUNREADDELTA,
    FLDCOL_OE6_WATCHEDHIGH,
    FLDCOL_OE6_WATCHEDUNREAD,
    FLDCOL_OE6_WATCHED,
    FLDCOL_OE6_LAST,
} FLDCOLID_OE6;

typedef struct tagFOLDERINFO_OE6 {
    BYTE               *pAllocated;
    BYTE                bVersion;
    FOLDERID            idFolder;
    FOLDERID            idParent;
    LPSTR               pszName;
    LPSTR               pszFile;
    LPSTR               pszDescription;
    LPSTR               pszAccountId;           // Server Nodes Only
    LPSTR               pszUrlComponent;
    FLDRFLAGS           dwFlags;
    DWORD               cMessages;
    DWORD               cUnread;
    DWORD               cWatched;
    DWORD               cThreadUnreadOld;
    DWORD               cViewUnreadOld;
    DWORD               cWatchedUnread;
    SPECIALFOLDER       tySpecial;
    FOLDERTYPE          tyFolder;
    BYTE                bHierarchy;
    DWORD               dwListStamp;
    DWORD               dwServerHigh;           // highest numbered article on server (news)
    DWORD               dwServerLow;            // lowest numbered article on server (news)
    DWORD               dwServerCount;          // count of articles on server (news)
    DWORD               dwClientHigh;           // highest numbered article known to client (news)
    DWORD               dwClientLow;            // lowest numbered article known to client (news)
    DWORD               dwStatusMsgDelta;       // total number of msgs added via STATUS resp. (IMAP)
    DWORD               dwStatusUnreadDelta;    // number of unread added via STATUS resp. (IMAP)
    DWORD               dwNotDownloaded;
    BLOB                Requested;
    BLOB                Read;
    DWORD               dwClientWatchedHigh;    // Highest numbered article we've checked for watch info (news)
} FOLDERINFO_OE6, *LPFOLDERINFO_OE6;

BEGIN_COLUMN_ARRAY(g_rgOE6FldTblColumns, FLDCOL_OE6_LAST)
    DEFINE_COLUMN(FLDCOL_OE6_ID,                 CDT_UNIQUE,  FOLDERINFO_OE6, idFolder)
    DEFINE_COLUMN(FLDCOL_OE6_PARENT,             CDT_DWORD,   FOLDERINFO_OE6, idParent)
    DEFINE_COLUMN(FLDCOL_OE6_NAME,               CDT_VARSTRA, FOLDERINFO_OE6, pszName)
    DEFINE_COLUMN(FLDCOL_OE6_FILE,               CDT_VARSTRA, FOLDERINFO_OE6, pszFile)
    DEFINE_COLUMN(FLDCOL_OE6_DESCRIPTION,        CDT_VARSTRA, FOLDERINFO_OE6, pszDescription)
    DEFINE_COLUMN(FLDCOL_OE6_ACCOUNTID,          CDT_VARSTRA, FOLDERINFO_OE6, pszAccountId)
    DEFINE_COLUMN(FLDCOL_OE6_FLAGS,              CDT_FLAGS,   FOLDERINFO_OE6, dwFlags)
    DEFINE_COLUMN(FLDCOL_OE6_MESSAGES,           CDT_DWORD,   FOLDERINFO_OE6, cMessages)
    DEFINE_COLUMN(FLDCOL_OE6_UNREAD,             CDT_DWORD,   FOLDERINFO_OE6, cUnread)
    DEFINE_COLUMN(FLDCOL_OE6_SPECIAL,            CDT_BYTE,    FOLDERINFO_OE6, tySpecial)
    DEFINE_COLUMN(FLDCOL_OE6_TYPE,               CDT_BYTE,    FOLDERINFO_OE6, tyFolder)
    DEFINE_COLUMN(FLDCOL_OE6_HIERARCHY,          CDT_BYTE,    FOLDERINFO_OE6, bHierarchy)
    DEFINE_COLUMN(FLDCOL_OE6_LISTSTAMP,          CDT_DWORD,   FOLDERINFO_OE6, dwListStamp)
    DEFINE_COLUMN(FLDCOL_OE6_SERVERHIGH,         CDT_DWORD,   FOLDERINFO_OE6, dwServerHigh)
    DEFINE_COLUMN(FLDCOL_OE6_SERVERLOW,          CDT_DWORD,   FOLDERINFO_OE6, dwServerLow)
    DEFINE_COLUMN(FLDCOL_OE6_SERVERCOUNT,        CDT_DWORD,   FOLDERINFO_OE6, dwServerCount)
    DEFINE_COLUMN(FLDCOL_OE6_CLIENTHIGH,         CDT_DWORD,   FOLDERINFO_OE6, dwClientHigh)
    DEFINE_COLUMN(FLDCOL_OE6_CLIENTLOW,          CDT_DWORD,   FOLDERINFO_OE6, dwClientLow)
    DEFINE_COLUMN(FLDCOL_OE6_NOTDOWNLOADED,      CDT_DWORD,   FOLDERINFO_OE6, dwNotDownloaded)
    DEFINE_COLUMN(FLDCOL_OE6_REQUESTED,          CDT_VARBLOB, FOLDERINFO_OE6, Requested)
    DEFINE_COLUMN(FLDCOL_OE6_URLCOMPONENT,       CDT_VARSTRA, FOLDERINFO_OE6, pszUrlComponent)
    DEFINE_COLUMN(FLDCOL_OE6_READ,               CDT_VARBLOB, FOLDERINFO_OE6, Read)
    DEFINE_COLUMN(FLDCOL_OE6_THREADUNREAD,       CDT_DWORD,   FOLDERINFO_OE6, cThreadUnreadOld)
    DEFINE_COLUMN(FLDCOL_OE6_VIEWUNREAD,         CDT_DWORD,   FOLDERINFO_OE6, cViewUnreadOld)
    DEFINE_COLUMN(FLDCOL_OE6_STATUSMSGDELTA,     CDT_DWORD,   FOLDERINFO_OE6, dwStatusMsgDelta)
    DEFINE_COLUMN(FLDCOL_OE6_STATUSUNREADDELTA,  CDT_DWORD,   FOLDERINFO_OE6, dwStatusUnreadDelta)
    DEFINE_COLUMN(FLDCOL_OE6_WATCHEDHIGH,        CDT_DWORD,   FOLDERINFO_OE6, dwClientWatchedHigh)
    DEFINE_COLUMN(FLDCOL_OE6_WATCHEDUNREAD,      CDT_DWORD,   FOLDERINFO_OE6, cWatchedUnread)
    DEFINE_COLUMN(FLDCOL_OE6_WATCHED,            CDT_DWORD,   FOLDERINFO_OE6, cWatched)
END_COLUMN_ARRAY

BEGIN_SYMBOL_TABLE(g_OE6FldSymbolTable, 2)
    DEFINE_SYMBOL(SYMBOL_DWORD, "FOLDER_SUBSCRIBED", FOLDER_SUBSCRIBED)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "FLDCOL_FLAGS", FLDCOL_OE6_FLAGS)
END_SYMBOL_TABLE

BEGIN_TABLE_INDEX(g_OE6FldTblPrimaryIndex, 1)
    DEFINE_KEY(FLDCOL_OE6_ID, 0, 0)
END_TABLE_INDEX


BEGIN_TABLE_SCHEMA(g_OE6FolderTableSchema, CLSID_FolderDatabase_OE6, FOLDERINFO_OE6)
    SCHEMA_PROPERTY(FOLDER_DATABASE_VERSION_OE6)
    SCHEMA_PROPERTY(TSF_RESETIFBADVERSION | TSF_HASEXTENSION)
    SCHEMA_PROPERTY(sizeof(STOREUSERDATA_OE6))
    SCHEMA_PROPERTY(offsetof(FOLDERINFO_OE6, idFolder))
    SCHEMA_PROPERTY(FLDCOL_OE6_LAST)
    SCHEMA_PROPERTY(g_rgOE6FldTblColumns)
    SCHEMA_PROPERTY(&amp;g_OE6FldTblPrimaryIndex)
    SCHEMA_PROPERTY(&amp;g_OE6FldSymbolTable)
    SCHEMA_PROPERTY(NULL) // Secondary indices
END_TABLE_SCHEMA

extern const TABLESCHEMA g_OE6FolderTableSchema;

const DWORD MESSAGE_DATABASE_VERSION_OE6 = 5;
const DWORD CB_COLUMNS_OE6               = 256;

typedef enum tagMSGTABLECOLID_OE6 {
    MSGCOL_OE6_ID=0,
    MSGCOL_OE6_FLAGS,
    MSGCOL_OE6_DATE,
    MSGCOL_OE6_LINECOUNT,
    MSGCOL_OE6_STREAM,
    MSGCOL_OE6_NORMALSUBJ,
    MSGCOL_OE6_DOWNLOADTIME,
    MSGCOL_OE6_MESSAGEID,
    MSGCOL_OE6_SUBJECT,
    MSGCOL_OE6_FROMHEADER,
    MSGCOL_OE6_REFERENCES,
    MSGCOL_OE6_XREF,
    MSGCOL_OE6_SERVER,
    MSGCOL_OE6_DISPLAYFROM,
    MSGCOL_OE6_EMAILFROM,
    MSGCOL_OE6_LANGUAGE,
    MSGCOL_OE6_PRIORITY,
    MSGCOL_OE6_SIZE,
    MSGCOL_OE6_RECEIVEDDATE,
    MSGCOL_OE6_DISPLAYTO,
    MSGCOL_OE6_EMAILTO,
    MSGCOL_OE6_PARTIALINFO,
    MSGCOL_OE6_POP3UIDL,
    MSGCOL_OE6_USERNAMEOLD,
    MSGCOL_OE6_PARTIALID,
    MSGCOL_OE6_FORWARDTO,
    MSGCOL_OE6_ACCOUNTNAME,
    MSGCOL_OE6_ACCOUNTID,
    MSGCOL_OE6_OFFSETTABLE,
    MSGCOL_OE6_HIGHLIGHT,
    MSGCOL_OE6_FOLDER,
    MSGCOL_OE6_FINDFOLDER,
    MSGCOL_OE6_FINDSOURCE,
    MSGCOL_OE6_PARENTOLD,
    MSGCOL_OE6_THREADIDOLD,
    MSGCOL_OE6_URLCOMPONENT,
    MSGCOL_OE6_STREAMIDOLD,
    MSGCOL_OE6_VERSION,
    MSGCOL_OE6_MSOESREC,
    MSGCOL_OE6_LASTID
} MSGTABLECOLID_OE6;

typedef struct tagFOLDERUSERDATA_OE6 {
    DWORD               fInitialized;                   // 4   Has this folder been initialized yet
    FOLDERTYPE          tyFolder;                       // the folder type
    CHAR                szAcctId[CCHMAX_ACCOUNT_NAME];  // 276 Account Id that folder belongs to
    CHAR                szFolder[CCHMAX_FOLDER_NAME];   // 532 Folder Name
    SPECIALFOLDER       tySpecial;                      // 536 Special Folder Type
    DWORD               fSubscribed;                    // 540 Is the folder subscribed ?
    DWORD               idSort;                         // 544 Current View Sort Order
    DWORD               fAscending;                     // 548 Current view is ascending ?
    DWORD               fThreaded;                      // 552 Current view is threaded
    RULEID              ridFilter;                      // 556 Current Filter for this Folder
    DWORD               dwFilterVersion;                // 560 Version of the filter
    FOLDERID            idFolder;                       // 564 Id of this folder
    DWORD               fWelcomeAdded;                  // 568 I have already added a welcome message...
    DWORD               dwUIDValidity;                  // 572 IMAP: Tells us if current acache is invalid
    DWORD               idMsgSelected;                  // The last Selected row
    BYTE                rgbColumns[CB_COLUMNS_OE6];         // Persisted Column Set
    DWORD               dwReserved1;                    // Used for sorting children
    DWORD               dwReserved2;                    // Reserved
    DWORD               fExpandAll;                     // Expand All Threads?
    DWORD               dwReserved3;                    // Do we have a dead filter?
    BYTE                fViewCounts;                    // Converted to view counts
    BYTE                fNewThreadModel;                // Converted to shared stream table ?
    BYTE                fWatchedCounts;                 // Converted to watched unread counts?
    BYTE                fTotalWatched;                  // Total Watched has been migrated.
    BYTE                fShowDeleted;                   // Current view shows deleted messages
    BYTE                fShowReplies;                   // Current view shows message replies
    BYTE                fNoIndexes;                     // No more indexes
    BYTE                rgReserved[717];                // Reserved
} FOLDERUSERDATA_OE6, *LPFOLDERUSERDATA_OE6;

typedef struct tagMESSAGEINFO_OE6 {
    BYTE               *pAllocated;
    BYTE                bVersion;
    DWORD_PTR           dwReserved;
    MESSAGEID           idMessage;
    MESSAGEFLAGS        dwFlags;
    FILETIME            ftSent;
    DWORD               cLines;
    FILEADDRESS         faStream;
    DWORD               idStreamOld;
    LPSTR               pszNormalSubj;
    FILETIME            ftDownloaded;
    LPSTR               pszMessageId;
    LPSTR               pszSubject;
    LPSTR               pszFromHeader;
    LPSTR               pszReferences;
    LPSTR               pszXref;
    LPSTR               pszServer;
    LPSTR               pszDisplayFrom;
    LPSTR               pszEmailFrom;
    WORD                wLanguage;
    WORD                wPriority;          // IMSGPRIORITY
    DWORD               cbMessage;
    FILETIME            ftReceived;
    LPSTR               pszDisplayTo;
    LPSTR               pszEmailTo;
    DWORD               dwPartial;          // Set to MESSAGE_COMBINED to indicate its a combined message
    LPSTR               pszUidl;
    LPSTR               pszUserNameOld;
    LPSTR               pszPartialId;
    LPSTR               pszForwardTo;
    LPSTR               pszAcctName;
    LPSTR               pszAcctId;
    LPSTR               pszUrlComponent;
    BLOB                Offsets;
    WORD                wHighlight;
    LPSTR               pszFolder;          // Only used in a find folder
    DWORD               iFindFolder;        // Only used in a find folder
    MESSAGEID           idFindSource;       // Only used in a find folder
    MESSAGEID           idParentOld;        // Used for Message Threading
    BLOB                ThreadIdOld;        // Used for custom threaded view
    BYTE                bUnused;            // The major version of oe in which this was downloaded by
    LPSTR               pszMSOESRec;
} MESSAGEINFO_OE6, *LPMESSAGEINFO_OE6;

BEGIN_COLUMN_ARRAY(g_rgOE6MsgTblColumns, MSGCOL_OE6_LASTID)
    DEFINE_COLUMN(MSGCOL_OE6_ID,            CDT_UNIQUE,   MESSAGEINFO_OE6, idMessage)
    DEFINE_COLUMN(MSGCOL_OE6_FLAGS,         CDT_FLAGS,    MESSAGEINFO_OE6, dwFlags)
    DEFINE_COLUMN(MSGCOL_OE6_DATE,          CDT_FILETIME, MESSAGEINFO_OE6, ftSent)
    DEFINE_COLUMN(MSGCOL_OE6_LINECOUNT,     CDT_DWORD,    MESSAGEINFO_OE6, cLines)
    DEFINE_COLUMN(MSGCOL_OE6_STREAM,        CDT_STREAM,   MESSAGEINFO_OE6, faStream)
    DEFINE_COLUMN(MSGCOL_OE6_NORMALSUBJ,    CDT_VARSTRA,  MESSAGEINFO_OE6, pszNormalSubj)
    DEFINE_COLUMN(MSGCOL_OE6_DOWNLOADTIME,  CDT_FILETIME, MESSAGEINFO_OE6, ftDownloaded)
    DEFINE_COLUMN(MSGCOL_OE6_MESSAGEID,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszMessageId)
    DEFINE_COLUMN(MSGCOL_OE6_SUBJECT,       CDT_VARSTRA,  MESSAGEINFO_OE6, pszSubject)
    DEFINE_COLUMN(MSGCOL_OE6_FROMHEADER,    CDT_VARSTRA,  MESSAGEINFO_OE6, pszFromHeader)
    DEFINE_COLUMN(MSGCOL_OE6_REFERENCES,    CDT_VARSTRA,  MESSAGEINFO_OE6, pszReferences)
    DEFINE_COLUMN(MSGCOL_OE6_XREF,          CDT_VARSTRA,  MESSAGEINFO_OE6, pszXref)
    DEFINE_COLUMN(MSGCOL_OE6_SERVER,        CDT_VARSTRA,  MESSAGEINFO_OE6, pszServer)
    DEFINE_COLUMN(MSGCOL_OE6_DISPLAYFROM,   CDT_VARSTRA,  MESSAGEINFO_OE6, pszDisplayFrom)
    DEFINE_COLUMN(MSGCOL_OE6_EMAILFROM,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszEmailFrom)
    DEFINE_COLUMN(MSGCOL_OE6_LANGUAGE,      CDT_WORD,     MESSAGEINFO_OE6, wLanguage)
    DEFINE_COLUMN(MSGCOL_OE6_PRIORITY,      CDT_WORD,     MESSAGEINFO_OE6, wPriority)
    DEFINE_COLUMN(MSGCOL_OE6_SIZE,          CDT_DWORD,    MESSAGEINFO_OE6, cbMessage)
    DEFINE_COLUMN(MSGCOL_OE6_RECEIVEDDATE,  CDT_FILETIME, MESSAGEINFO_OE6, ftReceived)
    DEFINE_COLUMN(MSGCOL_OE6_DISPLAYTO,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszDisplayTo)
    DEFINE_COLUMN(MSGCOL_OE6_EMAILTO,       CDT_VARSTRA,  MESSAGEINFO_OE6, pszEmailTo)
    DEFINE_COLUMN(MSGCOL_OE6_PARTIALINFO,   CDT_DWORD,    MESSAGEINFO_OE6, dwPartial)
    DEFINE_COLUMN(MSGCOL_OE6_POP3UIDL,      CDT_VARSTRA,  MESSAGEINFO_OE6, pszUidl)
    DEFINE_COLUMN(MSGCOL_OE6_USERNAMEOLD,   CDT_VARSTRA,  MESSAGEINFO_OE6, pszUserNameOld)
    DEFINE_COLUMN(MSGCOL_OE6_PARTIALID,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszPartialId)
    DEFINE_COLUMN(MSGCOL_OE6_FORWARDTO,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszForwardTo)
    DEFINE_COLUMN(MSGCOL_OE6_ACCOUNTNAME,   CDT_VARSTRA,  MESSAGEINFO_OE6, pszAcctName)
    DEFINE_COLUMN(MSGCOL_OE6_ACCOUNTID,     CDT_VARSTRA,  MESSAGEINFO_OE6, pszAcctId)
    DEFINE_COLUMN(MSGCOL_OE6_OFFSETTABLE,   CDT_VARBLOB,  MESSAGEINFO_OE6, Offsets)
    DEFINE_COLUMN(MSGCOL_OE6_HIGHLIGHT,     CDT_WORD,     MESSAGEINFO_OE6, wHighlight)
    DEFINE_COLUMN(MSGCOL_OE6_FOLDER,        CDT_VARSTRA,  MESSAGEINFO_OE6, pszFolder)
    DEFINE_COLUMN(MSGCOL_OE6_FINDFOLDER,    CDT_DWORD,    MESSAGEINFO_OE6, iFindFolder)
    DEFINE_COLUMN(MSGCOL_OE6_FINDSOURCE,    CDT_DWORD,    MESSAGEINFO_OE6, idFindSource)
    DEFINE_COLUMN(MSGCOL_OE6_PARENTOLD,     CDT_DWORD,    MESSAGEINFO_OE6, idParentOld)
    DEFINE_COLUMN(MSGCOL_OE6_THREADIDOLD,   CDT_VARBLOB,  MESSAGEINFO_OE6, ThreadIdOld)
    DEFINE_COLUMN(MSGCOL_OE6_URLCOMPONENT,  CDT_VARSTRA,  MESSAGEINFO_OE6, pszUrlComponent)
    DEFINE_COLUMN(MSGCOL_OE6_STREAMIDOLD,   CDT_DWORD,    MESSAGEINFO_OE6, idStreamOld)
    DEFINE_COLUMN(MSGCOL_OE6_VERSION,       CDT_BYTE,     MESSAGEINFO_OE6, bUnused)
    DEFINE_COLUMN(MSGCOL_OE6_MSOESREC,      CDT_VARSTRA,  MESSAGEINFO_OE6, pszMSOESRec)
END_COLUMN_ARRAY

BEGIN_TABLE_INDEX(g_OE6MsgTblPrimaryIndex, 1)
    DEFINE_KEY(MSGCOL_OE6_ID, 0, 0)
END_TABLE_INDEX

BEGIN_SYMBOL_TABLE(g_OE6MsgSymbolTable, 21)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_READ", ARF_READ)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_HASBODY", ARF_HASBODY)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_ENDANGERED", ARF_ENDANGERED)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_FLAGS", MSGCOL_OE6_FLAGS)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_EMAILFROM", MSGCOL_OE6_EMAILFROM)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_WATCH", ARF_WATCH)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_IGNORE", ARF_IGNORE)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_HASATTACH", ARF_HASATTACH)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_SIGNED", ARF_SIGNED)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_ENCRYPTED", ARF_ENCRYPTED)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_PRIORITY", MSGCOL_OE6_PRIORITY)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_SUBJECT", MSGCOL_OE6_SUBJECT)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_FROMHEADER", MSGCOL_OE6_FROMHEADER)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_ACCOUNTID", MSGCOL_OE6_ACCOUNTID)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_LINECOUNT", MSGCOL_OE6_LINECOUNT)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "IMSG_PRI_HIGH", IMSG_PRI_HIGH)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "IMSG_PRI_LOW", IMSG_PRI_LOW)
    DEFINE_SYMBOL(SYMBOL_COLUMN, "MSGCOL_DISPLAYFROM", MSGCOL_OE6_DISPLAYFROM)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_FLAGGED", ARF_FLAGGED)
    DEFINE_SYMBOL(SYMBOL_METHOD, "MessageAgeInDays", METHODID_MESSAGEAGEINDAYS)
    DEFINE_SYMBOL(SYMBOL_DWORD,  "ARF_DELETED_OFFLINE", ARF_DELETED_OFFLINE)
END_SYMBOL_TABLE

BEGIN_TABLE_SCHEMA(g_OE6MessageTableSchema, CLSID_MessageDatabase_OE6, MESSAGEINFO_OE6)
    SCHEMA_PROPERTY(MESSAGE_DATABASE_VERSION_OE6)
    SCHEMA_PROPERTY(TSF_HASSTREAMS | TSF_RESETIFBADVERSION)
    SCHEMA_PROPERTY(sizeof(FOLDERUSERDATA_OE6))
    SCHEMA_PROPERTY(offsetof(MESSAGEINFO_OE6, idMessage))
    SCHEMA_PROPERTY(MSGCOL_OE6_LASTID)
    SCHEMA_PROPERTY(g_rgOE6MsgTblColumns)
    SCHEMA_PROPERTY(&amp;g_OE6MsgTblPrimaryIndex)
    SCHEMA_PROPERTY(&amp;g_OE6MsgSymbolTable)
    SCHEMA_PROPERTY(NULL) // Secondary indices
END_TABLE_SCHEMA

extern const TABLESCHEMA g_OE6MessageTableSchema;

const DWORD POP3UIDL_DATABASE_VERSION_OE6   = 5;

typedef enum tagUIDLCOLID_OE6 {
    UIDLCOL_OE6_DLTIME,
    UIDLCOL_OE6_DELETED,
    UIDLCOL_OE6_DOWNLOADED,
    UIDLCOL_OE6_UIDL,
    UIDLCOL_OE6_SERVER,
    UIDLCOL_OE6_ACCOUNTID,
    UIDLCOL_OE6_LAST
} UIDLCOLID_OE6;

typedef struct tagUIDLRECORD_OE6 {
    BYTE               *pAllocated;
    BYTE                bVersion;
    BYTE                fDownloaded;
    BYTE                fDeleted;
    FILETIME            ftDownload;
    LPSTR               pszUidl;
    LPSTR               pszServer;
    LPSTR               pszAccountId;
} UIDLRECORD_OE6, *LPUIDLRECORD_OE6;

BEGIN_COLUMN_ARRAY(g_rgOE6UidlTblColumns, UIDLCOL_OE6_LAST)
    DEFINE_COLUMN(UIDLCOL_OE6_DLTIME,     CDT_FILETIME, UIDLRECORD_OE6, ftDownload)
    DEFINE_COLUMN(UIDLCOL_OE6_DELETED,    CDT_BYTE,     UIDLRECORD_OE6, fDeleted)
    DEFINE_COLUMN(UIDLCOL_OE6_DOWNLOADED, CDT_BYTE,     UIDLRECORD_OE6, fDownloaded)
    DEFINE_COLUMN(UIDLCOL_OE6_UIDL,       CDT_VARSTRA,  UIDLRECORD_OE6, pszUidl)
    DEFINE_COLUMN(UIDLCOL_OE6_SERVER,     CDT_VARSTRA,  UIDLRECORD_OE6, pszServer)
    DEFINE_COLUMN(UIDLCOL_OE6_ACCOUNTID,  CDT_VARSTRA,  UIDLRECORD_OE6, pszAccountId)
END_COLUMN_ARRAY

BEGIN_TABLE_INDEX(g_OE6UidlTblPrimaryIndex, 3)
    DEFINE_KEY(UIDLCOL_OE6_UIDL,     COMPARE_ASANSI,                      0)
    DEFINE_KEY(UIDLCOL_OE6_SERVER,   COMPARE_ASANSI | COMPARE_IGNORECASE, 0)
    DEFINE_KEY(UIDLCOL_OE6_ACCOUNTID,COMPARE_ASANSI | COMPARE_IGNORECASE, 0)
END_TABLE_INDEX

BEGIN_TABLE_SCHEMA(g_OE6UidlTableSchema, CLSID_Pop3UidlDatabase, UIDLRECORD_OE6)
    SCHEMA_PROPERTY(POP3UIDL_DATABASE_VERSION_OE6)
    SCHEMA_PROPERTY(TSF_RESETIFBADVERSION)
    SCHEMA_PROPERTY(0)
    SCHEMA_PROPERTY(0xffffffff)
    SCHEMA_PROPERTY(UIDLCOL_OE6_LAST)
    SCHEMA_PROPERTY(g_rgOE6UidlTblColumns)
    SCHEMA_PROPERTY(&amp;g_OE6UidlTblPrimaryIndex)
    SCHEMA_PROPERTY(NULL)
    SCHEMA_PROPERTY(NULL) // Secondary indices
END_TABLE_SCHEMA

extern const TABLESCHEMA g_OE6UidlTableSchema;

const DWORD SYNCOP_DATABASE_VERSION_OE6 = 2;

typedef enum tagSYNCOPTABLECOLID_OE6 {
    OPCOL_OE6_ID = 0,
    OPCOL_OE6_SERVER,
    OPCOL_OE6_FOLDER,
    OPCOL_OE6_MESSAGE,
    OPCOL_OE6_OPTYPE,
    OPCOL_OE6_FLAGS,
    OPCOL_OE6_ADD_FLAGS,
    OPCOL_OE6_REMOVE_FLAGS,
    OPCOL_OE6_FOLDER_DEST,
    OPCOL_OE6_MESSAGE_DEST,
    OPCOL_OE6_LASTID
} SYNCOPTABLECOLID_OE6;

typedef struct tagSYNCOPUSERDATA_OE6 {
    DWORD               fInitialized;                   // 4   Has this folder been initialized yet
    BYTE                rgReserved[248];                // Reserved
} SYNCOPUSERDATA_OE6, *LPSYNCOPUSERDATA_OE6;

typedef struct tagSYNCOPINFO_OE6 {
    BYTE               *pAllocated;
    BYTE                bVersion;
    SYNCOPID            idOperation;
    FOLDERID            idServer;
    FOLDERID            idFolder;
    MESSAGEID           idMessage;
    SYNCOPTYPE          tyOperation;
    SYNCOPFLAGS         dwFlags;
    MESSAGEFLAGS        dwAdd;
    MESSAGEFLAGS        dwRemove;
    FOLDERID            idFolderDest;
    MESSAGEID           idMessageDest;
} SYNCOPINFO_OE6, *LPSYNCOPINFO_OE6;

BEGIN_COLUMN_ARRAY(g_rgOE6OpTblColumns, OPCOL_OE6_LASTID)
    DEFINE_COLUMN(OPCOL_OE6_ID,             CDT_DWORD,    SYNCOPINFO, idOperation)
    DEFINE_COLUMN(OPCOL_OE6_SERVER,         CDT_DWORD,    SYNCOPINFO, idServer)
    DEFINE_COLUMN(OPCOL_OE6_FOLDER,         CDT_DWORD,    SYNCOPINFO, idFolder)
    DEFINE_COLUMN(OPCOL_OE6_MESSAGE,        CDT_DWORD,    SYNCOPINFO, idMessage)
    DEFINE_COLUMN(OPCOL_OE6_OPTYPE,         CDT_WORD,     SYNCOPINFO, tyOperation)
    DEFINE_COLUMN(OPCOL_OE6_FLAGS,          CDT_DWORD,    SYNCOPINFO, dwFlags)
    DEFINE_COLUMN(OPCOL_OE6_ADD_FLAGS,      CDT_DWORD,    SYNCOPINFO, dwAdd)
    DEFINE_COLUMN(OPCOL_OE6_REMOVE_FLAGS,   CDT_DWORD,    SYNCOPINFO, dwRemove)
    DEFINE_COLUMN(OPCOL_OE6_FOLDER_DEST,    CDT_DWORD,    SYNCOPINFO, idFolderDest)
    DEFINE_COLUMN(OPCOL_OE6_MESSAGE_DEST,   CDT_DWORD,    SYNCOPINFO, idMessageDest)
END_COLUMN_ARRAY

BEGIN_TABLE_INDEX(g_OE6OpTblPrimaryIndex, 1)
    DEFINE_KEY(OPCOL_OE6_ID,        0,  0)
END_TABLE_INDEX

BEGIN_TABLE_SCHEMA(g_OE6SyncOpTableSchema, CLSID_SyncOpDatabase_OE6, SYNCOPINFO_OE6)
    SCHEMA_PROPERTY(SYNCOP_DATABASE_VERSION_OE6)
    SCHEMA_PROPERTY(TSF_RESETIFBADVERSION)
    SCHEMA_PROPERTY(sizeof(SYNCOPUSERDATA_OE6))
    SCHEMA_PROPERTY(offsetof(SYNCOPINFO_OE6, idOperation))
    SCHEMA_PROPERTY(OPCOL_OE6_LASTID)
    SCHEMA_PROPERTY(g_rgOE6OpTblColumns)
    SCHEMA_PROPERTY(&amp;g_OE6OpTblPrimaryIndex)
    SCHEMA_PROPERTY(NULL)
    SCHEMA_PROPERTY(NULL) // Secondary indices
END_TABLE_SCHEMA

extern const TABLESCHEMA g_OE6SyncOpTableSchema;
```



The following example header describes the synchronized operations references.


```
#pragma once

// {26FE9D30-1A8F-11d2-AABF-006097D474C4}
DEFINE_GUID(CLSID_SyncOpDatabase, 0x26fe9d30, 0x1a8f, 0x11d2, 0xaa, 0xbf, 0x0, 0x60, 0x97, 0xd4, 0x74, 0xc4);

DECLARE_HANDLE(SYNCOPID);
typedef SYNCOPID *LPSYNCOPID;

const SYNCOPID   SYNCOPID_INVALID = (SYNCOPID)-1;

const DWORD SYNCOP_DATABASE_VERSION = 2;

typedef enum tagSYNCOPTABLECOLID {
    OPCOL_ID = 0,
    OPCOL_SERVER,
    OPCOL_FOLDER,
    OPCOL_MESSAGE,
    OPCOL_OPTYPE,
    OPCOL_FLAGS,
    OPCOL_ADD_FLAGS,
    OPCOL_REMOVE_FLAGS,
    OPCOL_FOLDER_DEST,
    OPCOL_MESSAGE_DEST,
    OPCOL_LASTID
} SYNCOPTABLECOLID;

typedef struct tagSYNCOPUSERDATA {
    DWORD               fInitialized;                   // 4   Has this folder been initialized yet
    BYTE                rgReserved[248];                // Reserved
} SYNCOPUSERDATA, *LPSYNCOPUSERDATA;

typedef enum tagSYNCOPTYPE {
    SYNC_INVALID        = 0x0000,
    SYNC_SETPROP_MSG    = 0x0001,
    SYNC_CREATE_MSG     = 0x0002,
    SYNC_COPY_MSG       = 0x0004,
    SYNC_MOVE_MSG       = 0x0008,
    SYNC_DELETE_MSG     = 0x0010
} SYNCOPTYPE;

typedef DWORD SYNCOPFLAGS;
#define SOF_ALLFLAGS                 0x00000001

typedef struct tagSYNCOPINFO {
    BYTE               *pAllocated;
    BYTE                bVersion;
    SYNCOPID            idOperation;
    FOLDERID            idServer;
    FOLDERID            idFolder;
    MESSAGEID           idMessage;
    SYNCOPTYPE          tyOperation;
    SYNCOPFLAGS         dwFlags;
    MESSAGEFLAGS        dwAdd;
    MESSAGEFLAGS        dwRemove;
    FOLDERID            idFolderDest;
    MESSAGEID           idMessageDest;
} SYNCOPINFO, *LPSYNCOPINFO;

BEGIN_COLUMN_ARRAY(g_rgOpTblColumns, OPCOL_LASTID)
    DEFINE_COLUMN(OPCOL_ID,             CDT_DWORD,    SYNCOPINFO, idOperation)
    DEFINE_COLUMN(OPCOL_SERVER,         CDT_DWORD,    SYNCOPINFO, idServer)
    DEFINE_COLUMN(OPCOL_FOLDER,         CDT_DWORD,    SYNCOPINFO, idFolder)
    DEFINE_COLUMN(OPCOL_MESSAGE,        CDT_DWORD,    SYNCOPINFO, idMessage)
    DEFINE_COLUMN(OPCOL_OPTYPE,         CDT_WORD,     SYNCOPINFO, tyOperation)
    DEFINE_COLUMN(OPCOL_FLAGS,          CDT_DWORD,    SYNCOPINFO, dwFlags)
    DEFINE_COLUMN(OPCOL_ADD_FLAGS,      CDT_DWORD,    SYNCOPINFO, dwAdd)
    DEFINE_COLUMN(OPCOL_REMOVE_FLAGS,   CDT_DWORD,    SYNCOPINFO, dwRemove)
    DEFINE_COLUMN(OPCOL_FOLDER_DEST,    CDT_DWORD,    SYNCOPINFO, idFolderDest)
    DEFINE_COLUMN(OPCOL_MESSAGE_DEST,   CDT_DWORD,    SYNCOPINFO, idMessageDest)
END_COLUMN_ARRAY

BEGIN_TABLE_INDEX(g_OpTblPrimaryIndex, 1)
    DEFINE_KEY(OPCOL_ID,        0,  0)
END_TABLE_INDEX

BEGIN_TABLE_INDEX(g_OpFolderIdIndex, 3)
    DEFINE_KEY(OPCOL_SERVER,    0,  0)
    DEFINE_KEY(OPCOL_FOLDER,    0,  0)
    DEFINE_KEY(OPCOL_ID,        0,  0)
END_TABLE_INDEX

extern const TABLEINDEX g_OpFolderIdIndex;

BEGIN_TABLE_SCHEMA(g_SyncOpTableSchema, CLSID_SyncOpDatabase, SYNCOPINFO)
    SCHEMA_PROPERTY(SYNCOP_DATABASE_VERSION)
    SCHEMA_PROPERTY(TSF_RESETIFBADVERSION)
    SCHEMA_PROPERTY(sizeof(SYNCOPUSERDATA))
    SCHEMA_PROPERTY(offsetof(SYNCOPINFO, idOperation))
    SCHEMA_PROPERTY(OPCOL_LASTID)
    SCHEMA_PROPERTY(g_rgOpTblColumns)
    SCHEMA_PROPERTY(&amp;g_OpTblPrimaryIndex)
    SCHEMA_PROPERTY(NULL)
END_TABLE_SCHEMA

extern const TABLESCHEMA g_SyncOpTableSchema;
```



 

 






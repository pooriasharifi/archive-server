def respons_str(msg, data):
    switcher = {
        'wait': 'لطفا صبر کنید',
        'internal_server_error': 'خطای داخلی سرور',
        
        
        'duplicate_username': 'نام کاربری تکراری',
        'duplicate_file_number': 'شماره پرونده تکراری',
        'duplicate_email': 'آدرس ایمیل تکراری',
        'duplicate_nationalـcode': 'کد ملی تکراری',
        'duplicate_attorneyـcode': 'کد وکالت تکراری',
        'duplicate_phone': 'شماره تلفن ثابت تکراری',
        'duplicate_mobile': 'شماره تلفن همراه تکراری',
        'duplicate_company_identification_email':'ایمیل سازمانی تکراری',
        'duplicate_birthـcertificate_code':'شماره شناسنامه تکراری',
        'dulpicate_insurance_number':'شماره بیمه تکراری',
        'dulpicate_recruitmentـcode':'کد کارگزینی تکراری',
        
        
        
        'username_required': 'عدم شناسایی نام کاربری',
        'name_required': 'عدم شناسایی نام',
        'last_name_required': 'عدم شناسایی نام خانوادگی',
        'password_required': 'عدم شناسایی رمز عبور',
        'birth_date_required': 'عدم شناسایی تاریخ تولد',
        'phone_required': 'عدم شناسایی شماره تلفن ثابت',
        'mobile_required': 'عدم شناسایی شماره تلفن همراه',
        'birthـcertificate_code_required': 'عدم شناسایی شماره شناسنامه',
        'father_name_required': 'عدم شناسایی نام پدر',
        'birth_certificate_serial_numberـrequired': 'عدم شناسایی شماره سریال شناسنامه',
        'insurance_number_required': 'عدم شناسایی شماره بیمه',
        'recruitmentـcode_required': 'عدم شناسایی کد کارگزینی',
        'address_required': 'عدم شناسایی آدرس',
        'company_identification_email_required':'عدم شناسایی ایمیل سازمانی',
        'no_content':'هیچ موردی وجود ندارد',

        
        
        'duplicate_title':'عنوان تکراری',
        'nationalـcode_invalid': 'کد ملی نامعتبر',
        'file_type_not_allowed': 'نوع فایل مجاز نیست',
        
        'registered': 'ثبت نام موفقیت آمیز',
        'logged': 'ورورد موفقیت آمیز',
        'incorrect_username_or_password': 'نام کاربری یا رمز عبور نامعتبر',
        'updated':'بروزرسانی موفقیت آمیز',
        'deleted':'حذف موفقیت آمیز',
        'user_not_found':'کاربر یافت نشد',
        
        
        
        'invalid_email_address':'آدرس ایمیل نامعتبر',
        'invalid_company_identification_number':'کد شناسایی شرکت نامعتبر',
        
        'duplicate_file_name':'فایل با این نام موجود است',
        'duplicate_title':'عنوان فایل موجود است',
        
        
        
        'upload_succes':'فایل با موفقیت بارگذاری شد',
        'succes':'عملیات موفقیت آمیز',

        'file_not_found':'پرونده یافت نشد',
        'national_code_not_found':'کد ملی یافت نشد',
        'registered_project': 'پروژه با موفقیت ثبت شد',
        'dulpicate_code_kala': 'کد کالا تکراری',
        'not_exist_kala': 'کالا وجود ندارد',
        'kala_edited': 'تغییرات کالا با موفقیت ثبت شد',
        'kala_deleted': 'کالا با موفقیت حذف شد',
        'connect': 'به سرور متصل شدید',
        'not_found': 'کاربر یافت نشد',
        'total_id_not':'شماره شناسایی کل یافت نشد',
        'mehvar_id_not':'شماره شناسایی محور یافت نشد',
        'subject_id_not':'شماره شناسایی موضوع یافت نشد',
        'img_success':'تصویر با موفقیت بارگذاری شد',
        'duplicate_group_id':'این گروه قبلا اضافه شده'
    }
    msg = switcher.get(msg, 'خطای سرور')
    return dict(
        msg=msg,
        data=data
    )

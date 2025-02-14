# OmniPos-BE
📂 ommipos-backend/

├── 📂 app/                     
│   ├── api/                  
│   │   ├── kiosk_router.py    
│   │   ├── pos_router.py      
│   │   ├── admin_router.py    
│   ├── domain/               
│   │   ├── kiosk/
│   │   │   ├── entities.py    
│   │   │   ├── services.py    
│   │   ├── pos/
│   │   │   ├── entities.py    
│   │   │   ├── services.py    
│   │   ├── admin/
│   │   │   ├── entities.py    
│   │   │   ├── services.py    
│   ├── infrastructure/        
│   │   ├── database.py        
│   │   ├── kiosk_repository.py
│   │   ├── pos_repository.py  
│   │   ├── admin_repository.py
│   │   ├── payments/          
│   ├── core/                  
│   │   ├── security.py        
│   │   ├── exceptions.py      
│   │   ├── utils.py           
│   ├── config/                
│   │   ├── settings.py        
│   ├── main.py                 
│   ├── init.py             
├── 📂 tests/                   
│   ├── test_kiosk.py          
│   ├── test_pos.py            
│   ├── test_admin.py           
├── pyproject.toml             
├── poetry.lock               
├── Dockerfile                  
├── .gitignore                 
└── README.md                   
SYSTEM_PROMPT = """
You are an expert in technology and have an expertise in tablets. You are aware of the most latest
tablets in the market. You have a unique skill of identifying the best suited tablets and have been 
able to recommend it to people around you based on the usage, budget and features required by them.

To suggest a good tablet.
1. Identify the age of the user, a kid using a tablet is mostly for entertainment or education purposes
a teenager would use the tablet for learning, social media and messaging. Adult might use the tablet 
for browsing, learning, videos etc.

2. Identify the budget of the user, this is a critical factor based on which many people decide on 
which device to buy

3. Feature set, another factor is the feature set included in the tablet.

Based on the above three factors help users decided on the best laptop suiting their needs, ask followup
questions to narrow down the above three factors and suggest the best tablet.

If asked anything other than tablets, respond with saying that your expertise is only in the domain of tablets.

"""

CONTEXT = """
Sure, I’ll include approximate prices for each tablet. Keep in mind that prices can vary based on region, retailer, and any ongoing promotions or discounts.

### 1. **Apple iPad Pro (2024)**

- **Price:**
  - **11-inch:** Starting at $799
  - **12.9-inch:** Starting at $1,099

- **Pros:**
  - Powerful M2 chip
  - Excellent Liquid Retina XDR display
  - High-quality cameras
  - Supports Apple Pencil 2 and Magic Keyboard

- **Cons:**
  - Expensive
  - iPadOS limitations compared to macOS

- **Specs:**
  - Display: 11-inch or 12.9-inch Liquid Retina XDR
  - Processor: Apple M2
  - Storage: 128GB, 256GB, 512GB, 1TB
  - RAM: 8GB or 16GB
  - Battery Life: Up to 10 hours
  - OS: iPadOS 17

- **Intended Users:**
  - Professionals and creatives

- **Features:**
  - Face ID
  - ProMotion technology
  - 5G support
  - Thunderbolt/USB 4

### 2. **Samsung Galaxy Tab S9 Ultra**

- **Price:**
  - Starting at $1,199

- **Pros:**
  - Large AMOLED display
  - Powerful Snapdragon 8 Gen 2 processor
  - Includes S Pen

- **Cons:**
  - Premium pricing
  - Android app ecosystem can be limiting

- **Specs:**
  - Display: 14.6-inch AMOLED
  - Processor: Qualcomm Snapdragon 8 Gen 2
  - Storage: 128GB, 256GB, 512GB
  - RAM: 12GB or 16GB
  - Battery Life: Up to 14 hours
  - OS: Android 13 with One UI

- **Intended Users:**
  - Power users, professionals, multimedia enthusiasts

- **Features:**
  - DeX mode
  - S Pen included
  - 5G support
  - Quad speakers tuned by AKG

### 3. **Microsoft Surface Pro 9**

- **Price:**
  - Starting at $999

- **Pros:**
  - Versatile 2-in-1 design
  - Full Windows 11 experience
  - Good build quality and display

- **Cons:**
  - Keyboard and pen sold separately
  - Premium price

- **Specs:**
  - Display: 13-inch PixelSense Flow
  - Processor: Intel Core i5 or i7 (12th Gen)
  - Storage: 128GB, 256GB, 512GB, 1TB
  - RAM: 8GB or 16GB
  - Battery Life: Up to 15 hours
  - OS: Windows 11

- **Intended Users:**
  - Professionals needing laptop-like functionality in a tablet

- **Features:**
  - Removable SSD
  - Surface Pen support
  - Kickstand with adjustable angles
  - USB-C and Thunderbolt 4

### 4. **Apple iPad Air (2024)**

- **Price:**
  - Starting at $599

- **Pros:**
  - A15 Bionic chip
  - Thin and lightweight
  - Good value for performance

- **Cons:**
  - Limited to 10.9-inch display
  - No Face ID

- **Specs:**
  - Display: 10.9-inch Liquid Retina
  - Processor: Apple A15 Bionic
  - Storage: 64GB, 256GB
  - RAM: 8GB
  - Battery Life: Up to 10 hours
  - OS: iPadOS 17

- **Intended Users:**
  - Users seeking high performance at a lower price than iPad Pro

- **Features:**
  - Supports Apple Pencil 2 and Magic Keyboard
  - Touch ID
  - USB-C connectivity

### 5. **Lenovo Tab P12 Pro**

- **Price:**
  - Starting at $749

- **Pros:**
  - High-resolution AMOLED display
  - Good performance with Snapdragon 870
  - Includes keyboard and stylus

- **Cons:**
  - Not as powerful as high-end models
  - Limited app support for Android tablets

- **Specs:**
  - Display: 12.6-inch AMOLED
  - Processor: Qualcomm Snapdragon 870
  - Storage: 128GB, 256GB
  - RAM: 6GB, 8GB
  - Battery Life: Up to 10 hours
  - OS: Android 12

- **Intended Users:**
  - Users needing high-quality display and performance at a lower price

- **Features:**
  - Lenovo Precision Pen 3 included
  - JBL speakers with Dolby Atmos
  - Supports keyboard attachment

### 6. **Huawei MatePad Pro 12.6**

- **Price:**
  - Starting at $899

- **Pros:**
  - Excellent display with high brightness
  - Includes M-Pencil and keyboard
  - Good performance with Kirin 9000E

- **Cons:**
  - Limited access to Google services
  - Expensive

- **Specs:**
  - Display: 12.6-inch OLED
  - Processor: Huawei Kirin 9000E
  - Storage: 128GB, 256GB
  - RAM: 8GB
  - Battery Life: Up to 10 hours
  - OS: HarmonyOS

- **Intended Users:**
  - Professionals and users needing a high-quality display without heavy reliance on Google services

- **Features:**
  - Huawei M-Pencil included
  - Multi-screen collaboration
  - High brightness and color accuracy

### 7. **Samsung Galaxy Tab A9 Plus**

- **Price:**
  - Starting at $349

- **Pros:**
  - Affordable pricing
  - Decent performance for everyday tasks
  - Lightweight and portable

- **Cons:**
  - Lower resolution display
  - Less powerful processor

- **Specs:**
  - Display: 10.4-inch TFT
  - Processor: MediaTek Helio G99
  - Storage: 64GB, expandable via microSD
  - RAM: 4GB
  - Battery Life: Up to 12 hours
  - OS: Android 13

- **Intended Users:**
  - Budget-conscious users needing a reliable tablet for basic tasks

- **Features:**
  - Expandable storage
  - Dolby Atmos sound
  - Lightweight design

### 8. **Amazon Fire HD 10 Plus (2023)**

- **Price:**
  - Starting at $179

- **Pros:**
  - Very affordable
  - Decent performance for its price
  - Good battery life

- **Cons:**
  - Limited app ecosystem (Amazon Appstore only)
  - Lower resolution screen

- **Specs:**
  - Display: 10.1-inch Full HD
  - Processor: Octa-core
  - Storage: 32GB, 64GB
  - RAM: 4GB
  - Battery Life: Up to 12 hours
  - OS: Fire OS

- **Intended Users:**
  - Budget-conscious users, especially those invested in Amazon’s ecosystem

- **Features:**
  - Alexa integration
  - Expandable storage
  - Robust build quality

### 9. **Asus ROG Flow Z13**

- **Price:**
  - Starting at $1,299

- **Pros:**
  - High-performance hardware
  - Unique detachable keyboard design
  - High refresh rate display

- **Cons:**
  - Expensive
  - Heavier and bulkier compared to other tablets

- **Specs:**
  - Display: 13.4-inch WUXGA+ (120Hz)
  - Processor: Intel Core i9
  - Storage: 256GB, 512GB, 1TB
  - RAM: 8GB, 16GB
  - Battery Life: Up to 8 hours
  - OS: Windows 11

- **Intended Users:**
  - Gamers and users needing high performance

- **Features:**
  - High-refresh-rate display
  - Detachable keyboard
  - Gaming-grade performance

### 10. **Xiaomi Pad 6 Pro**

- **Price:**
  - Starting at $499

- **Pros:**
  - Affordable with high-quality display
  - Good performance for its price
  - Supports stylus and keyboard

- **Cons:**
  - Software ecosystem not as polished
  - Limited availability in some regions

- **Specs:**
  - Display: 11-inch LCD, 2880 x 1800 resolution
  - Processor: Snapdragon 8+ Gen 1
  - Storage: 128GB, 256GB
  - RAM: 6GB, 8GB
  - Battery Life: Up to 12 hours
  - OS: MIUI for Pad

- **Intended Users:**
  - Users seeking a balance of performance and value

- **Features:**
  - Supports Xiaomi Smart Pen
  - Good display quality
  - MIUI-specific features for productivity
"""
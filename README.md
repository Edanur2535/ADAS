# ROS2 Jazzy – ADAS Perception Project

Bu proje, **ROS2 Jazzy** kullanılarak geliştirilmiş bir **ADAS (Advanced Driver Assistance Systems) algılama (perception)** modülünü içermektedir. Proje Docker ortamında çalışacak şekilde yapılandırılmıştır ve Python tabanlı ROS2 node’larından oluşur.

---

## 📁 Proje Yapısı

```text
ros2_ws/
├── src/
│   ├── adas_msgs/                 # Özel mesaj tanımları (varsa)
│   └── adas_perception/
│       ├── adas_perception/
│       │   ├── camera_node.py
│       │   ├── mock_control_publisher.py
│       │   ├── listener.py
│       │   ├── talker.py
│       │   └── __init__.py
│       ├── launch/
│       │   └── system.launch.py
│       ├── config/
│       │   └── params.yaml
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
├── build/      # GitHub’a eklenmez
├── install/    # GitHub’a eklenmez
└── log/        # GitHub’a eklenmez
```

---

## 🚀 Çalıştırma Ortamı

* **ROS2 Dağıtımı:** Jazzy
* **Dil:** Python (ament_python)
* **Platform:** Docker (Linux container)
* **Geliştirme Ortamı:** VS Code + Dev Containers

---

## ⚙️ Kurulum Adımları

### 1️⃣ Repoyu klonla

```bash
git clone https://github.com/<kullanici_adi>/<repo_adi>.git
cd ros2_ws
```

### 2️⃣ Docker container içine gir

(İmaj adına göre değişebilir)

```bash
docker exec -it ros2_jazzy_container bash
```

### 3️⃣ Workspace’i build et

```bash
colcon build
source install/setup.bash
```

---

## ▶️ Sistemi Çalıştırma

Tüm sistemi tek seferde başlatmak için:

```bash
ros2 launch adas_perception system.launch.py
```

Bu launch dosyası şunları başlatır:

* `camera_node`
* `mock_control_publisher`

Parametreler:

* `config/params.yaml` dosyasından yüklenir

---

## 🧪 Tek Tek Node Çalıştırma

```bash
ros2 run adas_perception camera
ros2 run adas_perception mock_node
```

---

## 📝 Parametreler

Parametreler `config/params.yaml` dosyasında tanımlıdır.
Örnek:

```yaml
camera:
  fps: 30
  width: 640
  height: 480
```

---

## ❗ GitHub Notları

Aşağıdaki klasörler **bilerek GitHub’a eklenmez**:

* `build/`
* `install/`
* `log/`

`.gitignore` içinde tanımlıdır.

---

## 🔒 Veri Güvenliği

Bu repo, bilgisayar sıfırlanması veya Docker container silinmesi durumunda projenin kaybolmaması için oluşturulmuştur.

---

## ✨ Geliştirme Planları

* Gerçek kamera entegrasyonu
* ZED / RealSense desteği
* Algılama çıktılarının kontrol sistemine entegrasyonu
* ROS2 topic & QoS optimizasyonları

---

## 👩‍💻 Geliştirici

**Edanur Çınar**
ROS2 · Python · ADAS · Perception

---

> Bu README, Docker + ROS2 Jazzy ortamında çalışan ADAS perception projeleri için referans olacak şekilde hazırlanmıştır.

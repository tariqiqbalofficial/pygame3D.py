<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Jumping Castle 3D</title>
    <!-- Include Three.js library -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
<!-- game.html -->
{% extends 'base.html' %}

{% block content %}
    <canvas id="gameCanvas"></canvas>

    <script>
        // Three.js code for the 3D game
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('gameCanvas') });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        camera.position.z = 5;

        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();
    </script>
{% endblock %}

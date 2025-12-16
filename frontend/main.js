import './main.css';
// создание HTML карточки врача
function createDoctorCard(doctor) {
    const stars = Array.from({ length: 5 }, (_, i) =>
        i < doctor.rating
            ? '<span class="star star--fill">★</span>'
            : '<span class="star">☆</span>'
    ).join('');

    return `
        <article class="doc">
            <div class="doc__header">
                <div class="doc__img">
                    ${doctor.name.charAt(0)}
                </div>
                <div class="doc__info">
                    <h3 class="doc__name">${doctor.name}</h3>
                    <p class="doc__type">${doctor.specialty}</p>
                    <p class="doc__place">${doctor.clinic}</p>
                </div>
            </div>
            <div class="doc__rate">
                ${stars}
            </div>
            <blockquote class="doc__text">
                "${doctor.review}"
            </blockquote>
            <p class="doc__author">— ${doctor.reviewer}</p>
        </article>
    `;
}

// отображение списка врачей в DOM
function renderDoctors(doctors) {
    const container = document.getElementById('doctors-list');
    if (!container) return;

    if (doctors.length === 0) {
        container.innerHTML = '<p>Врачи не найдены</p>';
        return;
    }

    container.innerHTML = doctors.map(createDoctorCard).join('');
}

// запрос списка врачей с сервера
async function fetchDoctors() {
    try {
        const response = await fetch('/api/doctors/');
        const data = await response.json();
        renderDoctors(data.doctors);
    } catch (error) {
        console.error('Ошибка загрузки врачей:', error);
        const container = document.getElementById('doctors-list');
        if (container) {
            container.innerHTML = '<p>Ошибка загрузки данных</p>';
        }
    }
}

// запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', fetchDoctors);
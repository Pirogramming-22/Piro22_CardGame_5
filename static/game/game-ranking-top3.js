function generateRanking() {
    const userDataElements = document.querySelectorAll("#user-data li");
    const users = Array.from(userDataElements).map(el => ({
        username: el.dataset.username,
        points: parseInt(el.dataset.points, 10)
    }));

    const barContainer = document.getElementById("bar-container");
    const rankingList = document.getElementById("ranking-list");

    // 최대 점수 계산 (막대 높이 비율을 정하기 위해 사용)
    const maxPoints = Math.max(...users.map(user => user.points), 0);

    // 점수 기준 내림차순으로 정렬
    users.sort((a, b) => b.points - a.points);

    let currentRank = 1; 
    let lastScore = -1; 
    let rankSkip = 1; 

    // 막대와 랭킹 생성
    users.forEach((user, index) => {
        // 동점자가 있을 경우, 이전 순위를 동일하게 부여
        if (user.points === lastScore) {
            
            rankSkip++;
        } else {
            // 동점자가 아니라면 새로운 순위
            currentRank += rankSkip - 1;
            rankSkip = 1; 
        }

        const bar = document.createElement("div");
        bar.className = `bar bar${index + 1}`;
        const barHeight = Math.max((user.points / maxPoints) * 100, 0); 
        bar.style.height = `${barHeight}%`;

        
        bar.innerHTML = `${currentRank}위`; 

        barContainer.appendChild(bar);

        // 랭킹 리스트 생성 
        const rank = document.createElement("p");
        rank.textContent = `${currentRank}위: ${user.username} (${user.points}점)`;
        rankingList.appendChild(rank);

        
        lastScore = user.points;
    });
}

generateRanking();

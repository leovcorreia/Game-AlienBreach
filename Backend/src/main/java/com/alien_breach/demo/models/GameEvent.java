package com.alien_breach.demo.models;

public class GameEvent {

    private Long gameId;
    private String type;
    private Integer points;

    public GameEvent() {
    }

    public GameEvent(Long gameId, String type, Integer points) {
        this.gameId = gameId;
        this.type = type;
        this.points = points;
    }

    public Long getGameId() {
        return gameId;
    }

    public void setGameId(Long gameId) {
        this.gameId = gameId;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Integer getPoints() {
        return points;
    }

    public void setPoints(Integer points) {
        this.points = points;
    }

}
